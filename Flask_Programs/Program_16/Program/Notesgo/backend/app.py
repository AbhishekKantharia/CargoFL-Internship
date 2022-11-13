from flask import Flask, render_template, redirect, send_from_directory, request, flash, url_for,session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bootstrap import Bootstrap   
import os
import urllib
import re
from forms import AddNoteForm


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'storage'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///notes.db"
app.config['SECRET_KEY'] = 'any secret string'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = "username",
    MAIL_PASSWORD = "password",
))

mail = Mail(app)
db = SQLAlchemy(app)
Bootstrap(app)

class Notes(db.Model):
    '''
    A class that stores data related to the notes.
    like the title of the subject, semester, and the link
    to the pdfs.
    '''
    id = db.Column(db.Integer, primary_key=True)
    subjectTitle = db.Column(db.String(15), nullable=False)
    subjectName = db.Column(db.String(40), nullable=False)
    chapterName = db.Column(db.String(40), nullable=False)
    link = db.Column(db.String(120))
    dateUploaded = db.Column(db.DateTime, nullable=False, default=datetime.now())
    semester = db.Column(db.Integer, nullable=False)

regex = r"(/d/)([0-9,a-z,A-z,\-,_]+)"
# file_url = 'https://drive.google.com/uc?export=download&id=1msv4oWXD1Au2uTJlzQ0Ez7vFUSrX0oRN'

@app.route("/")
def home():
    '''
    Function returing the landing page.
    '''
    
    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST'])
def add():
    '''
    A input form for uploading new notes. User needs
    to enter the details and put the drive link to 
    the notes.
    '''
    form = AddNoteForm(request.form)
    if request.method == 'POST':
        note = Notes(subjectTitle = form.subjectTitle.data,
                    subjectName = form.subjectName.data,
                    chapterName = form.chapterName.data,
                    link = form.link.data, 
                    semester = form.semester.data
                )
        db.session.add(note)
        db.session.commit()
        flash('Note successfully added')
        return redirect('/')
    return render_template('notes-add.html', form=form)

@app.route('/notes', methods=['GET','POST'])
def notesListView():
    '''
    Shows the list of the notes based on the user's semester.

    '''
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        print(request)
        session['useremail'] = request.form['email']
        # import pdb; pdb.set_trace()
        notes = Notes.query.filter_by(semester=request.form['semester']).order_by(Notes.subjectTitle)
        content = {'notes':notes,
                   'semester': request.form['semester'],
                   'email': request.form['email'],
                   'name': request.form['name']}
        # import pdb; pdb.set_trace()
    return render_template('notes-list.html',content = content)

def sendmail(filenames):
    '''
    A function that takes in the downloaded files
    and send it to the recepient.

    parameters - filenames (path or the name of the file).

    '''

    msg = Message("Hello",
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients=[session.get('usermail', None)])

    msg.body = "Get up"
    msg.html = "<h1>Hello there </h1>"

    for filename in filenames:
        with app.open_resource(filename) as fp:
            msg.attach(filename, "application/pdf", fp.read())

    mail.send(msg)
    
    return str(msg)
    
@app.route('/send', methods=['GET', 'POST'])
def downloadAndMail():
    ''' 
    Function saving the pdf file from google drive.

    extract out the id from the link and convert it into 
    downloadable link format.

    If downloading is successfull, the file(s) is/are sent to the 
    recepient. Otherwise it returns and error message.


    # params
    filename : takes in the url of the pdf file.
    return : a string indicating a success or failure.
    '''

    
    if request.method == 'POST' and request.form.getlist("notes"):
        
        note_id = request.form.getlist("notes")
        notes = []
        filenames = []
        for i in note_id:
            notes.append(Notes.query.get(i))
        try:
            for note in notes:
                match = re.search(regex, note.link)
                downloadable_url = "https://drive.google.com/uc?export=download&id=" + str(match[2])
                filename = str(note.subjectName+"-"+note.chapterName+'.pdf')
                filenames.append(filename) 
                print(downloadable_url)
                # import pdb; pdb.set_trace()
                urllib.request.urlretrieve(downloadable_url, filename)
                download_status = 1
                # print(filenames)
            
            
        except Exception as e:
            print("Exception {e}")
            download_message = "Failed: " + str(e)  
            download_status = 0 
        
        if download_status:
            sendmail(filenames)
            flash("Files sent successfully",'success')

    elif request.method == 'POST' and not request.form.getlist("notes"):
        flash("You didn't selected any file.", 'warning')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
