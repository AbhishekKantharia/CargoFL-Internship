# import libraries
import sys
import nltk
import re
nltk.download(['punkt','wordnet'])
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline

from nltk.tokenize import word_tokenize, WhitespaceTokenizer

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.multioutput import MultiOutputClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
import pickle

def load_data(database_filepath):
    """ Load data from database,
    Define feature and target variables X and Y,
    Define categories list.
    
    Args:
        database_filepath (str): the database file path. 
        
    Returns: 
        df (dataframe): clean dataframe.
        X (dataframe): feature variable.
        Y (dataframe): target variable.
        category_names (list): list of message categories.
    
    """
        
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('Messages',engine) 
    X = df['message']
    Y = df.iloc[:,4:]
    category_names=Y.columns 
    df=df[~(df.isnull().any(axis=1))|((df.original.isnull())&~(df.offer.isnull()))]
    
    return X, Y, category_names
    
def tokenize(text):
    """using nltk to case normalize, lemmatize, and tokenize text. 
    This function is used in the machine learning pipeline to, 
    vectorize and then apply TF-IDF to the text.
    
     Args:
        text (str): A disaster message. 
        
    Returns: 
        processed_tokens (list): list of cleaned tokens in the message.
        
    """
    # get tokens from text
    tokens= WhitespaceTokenizer().tokenize(text)
    lemmatizer= WordNetLemmatizer()
    
    # clean tokens
    processed_tokens=[]
    for token in tokens:
        token=lemmatizer.lemmatize(token).lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        token=re.sub(r'\[[^.,;:]]*\]','', token)
        
        # add token to compiled list if not empty
        if token !='':
            processed_tokens.append(token)
    return processed_tokens


def build_model():
    """ Build a TF-IDF pipeline that,
    processes text and then performs,
    multi-output classification on the 36 categories in the dataset.
    
    Returns:
       cv (scikit-learn GridSearchCV):  GridSearchCV model object. 
       
    """
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer = tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(OneVsRestClassifier(LinearSVC())))
    ])
    
    parameters = {
    'tfidf__smooth_idf':[True, False],
    'clf__estimator__estimator__C':[1,2,5]}

    cv = GridSearchCV(pipeline, parameters)
    
    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    """ This function applies ML pipeline to a test set and prints out
    model performance (accuracy and f1score)
    
    Args:
        model (sklearn.model_selection.GridSearchCV): scikit ML pipeline.
        X_test (dataframe): test features.
        Y_test (dataframe): test labels.
        category_names (list): list of category names.
    """
    #make predictions with model
    Y_pred=model.predict(X_test)
    
    #print scores
    print(classification_report(Y_test.iloc[:,1:].values, np.array([x[1:] for x in Y_pred]), target_names=category_names))

def save_model(model, model_filepath):
    """ Save model as a pickle file.
    
    Args:
        model (sklearn.model_selection.GridSearchCV): scikit ML pipeline.
        model_filepath (str): destination path to save .pkl file.
        
     """
    pickle.dump(model.best_estimator_, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()