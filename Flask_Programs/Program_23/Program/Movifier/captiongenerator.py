#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:27:21 2019

@author: jacobwilkins
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf, matplotlib.pyplot as plt
import numpy as np, time
import CNN_Encoder, RNN_Decoder

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from PIL import Image

BATCH_SIZE = 64
BUFFER_SIZE = 1000
embedding_dim = 256
units = 512
# Shape of the vector extracted from InceptionV3 is (64, 2048)
# These two variables represent that vector shape
features_shape = 2048 
attention_features_shape = 64

EPOCHS = 20

class Captiongenerator(object):
    
    def __init__(self, img_names, img_captions):
        self.img_names = img_names
        self.img_captions = img_captions
        self.setup()
        
    def setup(self):
        train_captions, img_name_vector = shuffle(self.img_captions, self.img_names, random_state=1)
        image_model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')
        new_input = image_model.input
        hidden_layer = image_model.layers[-1].output
        
        self.image_features_extract_model = tf.keras.Model(new_input, hidden_layer)
        
        # Get unique images
        encode_train = sorted(set(img_name_vector))
        # Feel free to change batch_size according to your system configuration
        image_dataset = tf.data.Dataset.from_tensor_slices(encode_train)
        image_dataset = image_dataset.map(self.load_image, num_parallel_calls=tf.data.experimental.AUTOTUNE).batch(16)
        
        for img, path in image_dataset:
            batch_features = self.image_features_extract_model(img)
            batch_features = tf.reshape(batch_features, (batch_features.shape[0], -1, batch_features.shape[3]))
        
        for bf, p in zip(batch_features, path):
            path_of_feature = p.numpy().decode("utf-8")
            np.save(path_of_feature, bf.numpy())
        
        # Choose the top 5000 words from the vocabulary
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=5000,oov_token="<unk>",filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')
        self.tokenizer.fit_on_texts(train_captions)
        train_seqs = self.tokenizer.texts_to_sequences(train_captions)
            
        self.tokenizer.word_index['<pad>'] = 0
        self.tokenizer.index_word[0] = '<pad>'
            
        # Create the tokenized vectors
        train_seqs = self.tokenizer.texts_to_sequences(train_captions)
            
        # Pad each vector to the max_length of the captions
        # If you do not provide a max_length value, pad_sequences calculates it automatically
        cap_vector = tf.keras.preprocessing.sequence.pad_sequences(train_seqs, padding='post')
            
        # Calculates the max_length, which is used to store the attention weights
        self.max_length = self.calc_max_length(train_seqs)
            
        # Create training and validation sets using an 80-20 split
        img_name_train, img_name_val, cap_train, cap_val = train_test_split(img_name_vector,cap_vector,test_size=0.2,random_state=0)
        
        vocab_size = len(self.tokenizer.word_index) + 1
        num_steps = len(img_name_train) // BATCH_SIZE
        
        dataset = tf.data.Dataset.from_tensor_slices((img_name_train, cap_train))
    
        # Use map to load the numpy files in parallel
        dataset = dataset.map(lambda item1, item2: tf.numpy_function(
                self.map_func, [item1, item2], [tf.float32, tf.int32]),
                num_parallel_calls=tf.data.experimental.AUTOTUNE)
        
        # Shuffle and batch
        dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
            
        self.encoder = CNN_Encoder.CNN_Encoder(embedding_dim)
        self.decoder = RNN_Decoder.RNN_Decoder(embedding_dim, units, vocab_size)
            
        self.optimizer = tf.keras.optimizers.Adam()
        self.loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none')
        '''
        # CHECKPOINT
        checkpoint_path = "./checkpoints/train"
        ckpt = tf.train.Checkpoint(encoder=self.encoder,
                                   decoder=self.decoder,
                                   optimizer = self.optimizer)
        ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)
            
        start_epoch = 0
        if ckpt_manager.latest_checkpoint:
            start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])
                
        # TRAINING
            
        # adding this in a separate cell because if you run the training cell
        # many times, the loss_plot array will be reset
        loss_plot = []
    
        for epoch in range(start_epoch, EPOCHS):
            start = time.time()
            total_loss = 0
            
            for (batch, (img_tensor, target)) in enumerate(dataset):
                batch_loss, t_loss = self.train_step(img_tensor, target)
                total_loss += t_loss
            
                if batch % 100 == 0:
                    print ('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1, batch, batch_loss.numpy() / int(target.shape[1])))
            # storing the epoch end loss value to plot later
            loss_plot.append(total_loss / num_steps)
            
            if epoch % 5 == 0: ckpt_manager.save()
            
            print ('Epoch {} Loss {:.6f}'.format(epoch + 1,total_loss/num_steps))
            print ('Time taken for 1 epoch {} sec\n'.format(time.time() - start))
            
        # captions on the validation set
        rid = np.random.randint(0, len(img_name_val))
        image = img_name_val[rid]
        real_caption = ' '.join([self.tokenizer.index_word[i] for i in cap_val[rid] if i not in [0]])
        result, attention_plot = self.evaluate(image)
        
        print ('Real Caption:', real_caption)
        print ('Prediction Caption:', ' '.join(result))
        self.plot_attention(image, result, attention_plot)
        # opening the image
        Image.open(img_name_val[rid])
        '''
    def calc_max_length(self, tensor):
        return max(len(t) for t in tensor)
        
    def load_image(self, image_path):
        img = tf.io.read_file(image_path)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, (299, 299))
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        return img, image_path
        
    # Load the numpy files
    def map_func(self, img_name, cap):
        img_tensor = np.load(img_name.decode('utf-8')+'.npy')
        return img_tensor, cap
    
    def loss_function(self, real, pred):
        mask = tf.math.logical_not(tf.math.equal(real, 0))
        loss_ = self.loss_object(real, pred)
        
        mask = tf.cast(mask, dtype=loss_.dtype)
        loss_ *= mask
        
        return tf.reduce_mean(loss_)
        
    @tf.function
    def train_step(self, img_tensor, target):
        loss = 0
        
        # initializing the hidden state for each batch
        # because the captions are not related from image to image
        hidden = self.decoder.reset_state(batch_size=target.shape[0])
        
        dec_input = tf.expand_dims([self.tokenizer.word_index['<start>']] * BATCH_SIZE, 1)
        
        with tf.GradientTape() as tape:
            features = self.encoder(img_tensor)
        
            for i in range(1, target.shape[1]):
                # passing the features through the decoder
                predictions, hidden, _ = self.decoder(dec_input, features, hidden)
        
                loss += self.loss_function(target[:, i], predictions)
        
                # using teacher forcing
                dec_input = tf.expand_dims(target[:, i], 1)
        
        total_loss = (loss / int(target.shape[1]))
        trainable_variables = self.encoder.trainable_variables + self.decoder.trainable_variables
        gradients = tape.gradient(loss, trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, trainable_variables))
        return loss, total_loss
            
    def evaluate(self, image):
        attention_plot = np.zeros((self.max_length, attention_features_shape))
        
        hidden = self.decoder.reset_state(batch_size=1)
        temp_input = tf.expand_dims(self.load_image(image)[0], 0)
        img_tensor_val = self.image_features_extract_model(temp_input)
        img_tensor_val = tf.reshape(img_tensor_val, (img_tensor_val.shape[0], -1, img_tensor_val.shape[3]))
        
        features = self.encoder(img_tensor_val)
        
        dec_input = tf.expand_dims([self.tokenizer.word_index['<start>']], 0)
        result = []
        
        for i in range(self.max_length):
            predictions, hidden, attention_weights = self.decoder(dec_input, features, hidden)
        
            attention_plot[i] = tf.reshape(attention_weights, (-1, )).numpy()
        
            predicted_id = tf.argmax(predictions[0]).numpy()
            result.append(self.tokenizer.index_word[predicted_id])
        
            if self.tokenizer.index_word[predicted_id] == '<end>':
                return result, attention_plot
        
            dec_input = tf.expand_dims([predicted_id], 0)
        
        attention_plot = attention_plot[:len(result), :]
        return result, attention_plot
        
    def plot_attention(self, image, result, attention_plot):
        temp_image = np.array(Image.open(image))
        
        fig = plt.figure(figsize=(10, 10))
        
        len_result = len(result)
        for l in range(len_result):
            temp_att = np.resize(attention_plot[l], (8, 8))
            ax = fig.add_subplot(len_result//2, len_result//2, l+1)
            ax.set_title(result[l])
            img = ax.imshow(temp_image)
            ax.imshow(temp_att, cmap='gray', alpha=0.6, extent=img.get_extent())
        
        plt.tight_layout()
        plt.show()  
    
