from flask import Flask, render_template, url_for, send_from_directory, request
from requests import get
from config import key
from os.path import join

app = Flask(__name__)

@app.route('/')
def index():
	#print(request.remote_addr)
	response1 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'business'}).json()
	response2 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'entertainment'}).json()
	response3 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'general'}).json()
	response4 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'health'}).json()
	response5 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'science'}).json()
	response6 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'sports'}).json()
	response7 = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key, 'category' : 'technology'}).json()
	return render_template('index.html', response1 = response1, response2 = response2, response3 = response3, response4 = response4, response5 = response5, response6 = response6, response7 = response7)

@app.route('/search', methods=['POST'])
def search():
	response = get("https://newsapi.org/v2/everything", params={'apikey' : key, 'q' : request.form['searchBar']}).json()
	return render_template('search.html', response = response)

@app.route('/sources')
def sources():
	response = get("https://newsapi.org/v2/sources", params = {'apiKey' : key}).json()
	return render_template('sources.html', name = response)

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run()
