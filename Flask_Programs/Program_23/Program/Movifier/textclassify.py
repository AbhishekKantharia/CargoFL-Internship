#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:27:21 2019

@author: jacobwilkins
"""

import re, pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from nltk.stem import WordNetLemmatizer

class Textclassify(object):
    
    def __init__(self, trainData): self.trainData = trainData
    
    def preprocess(self, x):
        docs = []; stemmer = WordNetLemmatizer()
        for k in range(0, len(x)):
            doc = re.sub(r'\W', ' ', str(x[k])) # Remove all the special characters
            doc = re.sub(r'\s+[a-zA-Z]\s+', ' ', doc) # remove all single characters
            doc = re.sub(r'\^[a-zA-Z]\s+', ' ', doc) # Remove single characters from the start
            doc = re.sub(r'\s+', ' ', doc, flags=re.I) # Substituting multiple spaces with single space
            doc = re.sub(r'^b\s+', '', doc) # Removing prefixed 'b'
            doc = doc.lower() # Converting to Lowercase
            doc = doc.split() # Lemmatization
            doc = [stemmer.lemmatize(word) for word in doc]
            doc = ' '.join(doc); docs.append(doc)
        return docs
    
    def classify(self, testData):
        x_test = [testData]; x_train = []; y_train = []
        for d in self.trainData:
            for key in d:
                if key == 'text': x_train.append(d[key])
                if key == 'genres':
                    if d[key] == []: y_train.append('other')
                    else:
                        for i in d[key]: y_train.append(i['name']); break
                        
        x_train = self.preprocess(x_train); x_test = self.preprocess(x_test)
        
        trainData = pd.DataFrame({'plot': x_train, 'tags': y_train})
        testData = pd.DataFrame({'plot': x_test, 'tags': ['Comedy']})

        vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=3000)
        train_data_features = vectorizer.fit_transform(trainData['plot'])
        train_data_features = train_data_features.toarray()

        classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
        classifier = classifier.fit(train_data_features, trainData['tags'])
        
        test_data_features = vectorizer.transform(testData['plot'])
        test_data_features = test_data_features.toarray()
        pred = classifier.predict(test_data_features)
        
        return pred
