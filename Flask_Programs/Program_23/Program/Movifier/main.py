#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:26:44 2019

@author: jacobwilkins
"""
import os, csv, textsearch, textclassify, captiongenerator, shutil, time, re
from flask import Flask, render_template, flash
from forms import TextSearchForm, TextClassifyForm, ImageCaptionForm
from markupsafe import Markup
from ast import literal_eval
from werkzeug import secure_filename
from google_drive_downloader import GoogleDriveDownloader as gdd

GOOGLE_DRIVE = 'https://drive.google.com/file/d/1V3xKf69SHmuXMiGzrBc_oiJcJshyoyIG/view?usp=sharing'

movies = [] # holds the movie results from the TextSearchForm
trainData = []; classifyRes = [] # holds training data and results for text classification
imageCaption = [] # holds the results for image caption generation

shutil.rmtree('/temp/movie_index', ignore_errors=True) # remove directory before indexing restarts
ts = textsearch.Textsearch('/temp/movie_index') # initialize text search

# index each movie by title, description, genres, IMBD id, and poster path
with open('movies_metadata.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile); doc_times = []; count = 0
    for row in reader:
        doc_id = row['original_title']; body = row['overview']
        link = row['imdbId']; genres = row['genres']; poster = row['poster_path']
        ts.index(doc_id, {'text': body}, {'link': link}, {'poster': poster}) # index for text search
        trainData.append({'text': body, 'genres': literal_eval(genres),}) # index for text classification
        count += 1
        if count > 1000: break # only index first 1000 movies

# downlaid images from google drive to use for image caption training
if not os.path.exists(os.path.abspath('.') + '/' + 'Flicker8k_Dataset/'):
    gdd.download_file_from_google_drive(file_id='1V3xKf69SHmuXMiGzrBc_oiJcJshyoyIG',
                                        dest_path='./Flickr8k_Dataset.zip',
                                        unzip=True)
PATH = os.path.abspath('.') + '/Flicker8k_Dataset/' # path where images are stored
img_names = []; img_captions = [] # holds image paths and captions

# index image/caption pairs for image caption training
with open('Flickr8k.lemma.token.txt', 'r') as f:
    count = 0
    for line in f:
        line = line.split("\t", 1)
        if line[0].endswith("1"): # only index 1 caption per image
            img_names.append(PATH + line[0][:-2])
            caption = '<start> ' + line[1] + ' <end>'
            img_captions.append(caption)
            count += 1
        if count > 1000: break # only index first 1000 image/caption pairs

tc = textclassify.Textclassify(trainData) # initialize text classify
cg = captiongenerator.Captiongenerator(img_names, img_captions) # initialize caption generator

def textSearchQuery(descr, numRes): # search query submitted from TextSearchForm
    start = time.time()
    results, terms = ts.search(descr, 0, numRes) # execute search
    searchTime = time.time() - start
    movieData = results.get('results')
    
    terms = sorted(ts.parse_query(descr), key = len, reverse=True); regStr = ""; d2 = {}
    for term in terms: regStr += "(" + str(term) + ")|"
    if bool(movies): movies.clear() # make sure movies doesn't have data from previous search
    for res in movieData: # highlight the terms in the movie descriptions
        text = res[1].get('text')
        i = 0; output = ""; temp1 = ""; temp2 = ""
        for m in re.compile(r"%s" % regStr[:-1], re.I).finditer(text):
            output += "".join([text[i:m.start()], "<strong><span style='background-color:#FFFF00'>", text[m.start():text.find(' ', m.end())], "</span></strong>"])
            i = text.find(' ', m.end()); temp1 = output; temp2 = text[text.find(' ', m.end()):]
        s2 = "".join([temp1, temp2]); d1 = {'text': Markup(u"%s" % s2)}
        if not s2 == "":
            if not d1 == d2:
                res[1].update(d1); d2 = d1
        # alter links depending on length
        if len(res[0].get('link')) == 6: res[0].update({'link': "0" + res[0].get('link')})
        if len(res[0].get('link')) == 5: res[0].update({'link': "00" + res[0].get('link')})
        # add each result to movies dict
        movies.append(res) # resulting data to be displayed
    return results.get('total_hits', 0), searchTime # return search time and num of results for flash message

def textClassify(descr): # classify query submitted from TextClassify form
    start = time.time()
    pred = tc.classify(descr) # execute classification
    searchTime = time.time() - start
    
    if bool(classifyRes): classifyRes.clear()
    classifyRes.append(pred) # resulting data to be displayed
    return searchTime # return search time for flash message

def generateCaption(image_path, filename): # generate caption for image submitted from ImageCaptionForm
    start = time.time()
    result, attention_plot = cg.evaluate(image_path) # execute caption generation
    searchTime = time.time() - start
    
    #cg.plot_attention(image_path, result, attention_plot)
    if bool(imageCaption): imageCaption.clear()
    imageCaption.append({'caption': result, 'name': filename}) # resulting data to be displayed
    return searchTime # return search time for flash message

def allowed_file(filename): # only allow certain file types
    return '.' in filename and filename.split('.', 1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'D22B5C72F638152BB566B67B3CF76'
app.config['UPLOAD_FOLDER'] = os.path.abspath('.') + '/uploads/'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home(): # control text search page
    form = TextSearchForm()
    if form.validate_on_submit():
        total_hits, searchTime = textSearchQuery(form.movieDescription.data, form.numResults.data)
        flash(Markup(f'Query successfully submitted! Found <b>%s</b> results in <b>%0.3f</b> seconds!' % (total_hits, searchTime)), 'success')
    return render_template("home.html", form=form, movies=movies)

@app.route("/classify", methods=['GET', 'POST'])
def classify(): # control text classify page
    form = TextClassifyForm()
    if form.validate_on_submit():
        searchTime = textClassify(form.movieDescription.data)
        flash(Markup(f'Query successfully submitted! Found results in <b>%0.3f</b> seconds!' % searchTime), 'success')
    return render_template("classify.html", form=form, classifyRes=classifyRes)

@app.route("/caption", methods=['GET', 'POST'])
def caption(): # control image caption page
    form = ImageCaptionForm()
    if form.validate_on_submit():
        if form.image.data.filename == '':
            flash(f'No image selected')
        if form.image.data and allowed_file(form.image.data.filename):
            filename = secure_filename(form.image.data.filename) # generate secure filename for image
            image_path = app.config['UPLOAD_FOLDER'] + filename
            form.image.data.save(image_path) # save image
            searchTime = generateCaption(image_path, filename)
            flash(Markup(f"Image successfully submitted! Caption generated in <b>%0.3f</b> seconds!" % searchTime), 'success')
    return render_template("caption.html", form=form, imageCaption=imageCaption)
            
if __name__ == "__main__": app.run(debug = True)
