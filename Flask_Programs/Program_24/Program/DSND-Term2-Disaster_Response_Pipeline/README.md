# Disaster Response Pipeline Project

## Table of Contents
1. [Project Motivation](#motivation)
2. [File Descriptions](#files)
3. [Required Libraries](#libraries)
4. [Instructions](#instructions)


## Project Motivation <a name="motivation"></a>

This project focuses on applying data engineering skills to analyze disaster data from [Figure Eight](https://www.figure-eight.com/) to build a model for an application program interface (API) that classifies disaster messages. The model is used to categorize disaster events, so messages can be sent to an appropriate disaster relief agency. The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

## File Descriptions <a name="files"></a>
```

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py # The script takes the file paths of the two datasets and database, cleans the datasets, and stores the clean data into a SQLite database in the specified database file path.
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py #he script takes the database file path and model file path, creates and trains a classifier, and stores the classifier into a pickle file to the specified model file path
|- classifier.pkl  # saved model 

- README.md

```

## Required Libraries <a name="libraries"></a>

 - Machine Learning Libraries: Pandas, NumPy, Scikit-Learn
 - Natural Language Process Libraries: NLTK
 - SQLite Database Libraries: SQLalchemy
 - Web App libraries: Flask
 - Visualization libraries: Plotly

## Instructions <a name="instructions"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
