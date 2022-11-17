# import libraries
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """Load disaster messages and categories dataframes,
    and merge them into one dataframe.
    
    Args:
        messages_filepath (str): path of messages csv file.
        categories_filepath (str): path of categories csv file.
        
    Returns:
        df (dataframe): combined messages and categories dataframes into one datframe using the common id.   
  
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, left_on='id',right_on='id',how='outer')
    return df

def clean_data(df):
    """ Cleans dataframe 
    
    Splits the categories column into separate, clearly named columns, 
    converts values to binary, 
    and drops duplicates.
    
    Args:
        df (dataframe): combined messages and categories dataframe.
        
    Returns:
        df (dataframe): clean dataframe.
        
    """
    categories = df.categories.str.split(';', expand=True)
    row = categories.loc[0]
    category_colnames = row.apply(lambda x: x[:-2]).values.tolist()
    categories.columns = category_colnames
    categories.related.loc[categories.related=='related-2']='related-1'
    for column in categories:
        categories[column] = categories[column].astype(str).str[-1]
        categories[column] = pd.to_numeric(categories[column])
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    df.drop_duplicates(subset='id', inplace=True)
    return df

def save_data(df, database_filename):
    """ Stores the clean data into a SQLite database,
    in the specified database file path.
    
    Args:
        df (dataframe): clean data.
        database_filename (str): destination path to SQLite database file.
        
     """
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('Messages', engine, index=False)

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()