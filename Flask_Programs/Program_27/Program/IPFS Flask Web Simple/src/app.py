from operator import and_
from flask import Flask
from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import ForeignKey
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import ipfsApi
import os
import webbrowser

UPLOAD_FOLDER = r'static\uploads'

app = Flask(__name__)
app.secret_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c2VyLTFTTTRSUTlfLS1IVEpGM0QiLCJpYXQiOjE2NjI5ODc0Nzd9.mCvSd2o2vw5Gs7grkBLkW75dlgVcJ-aiqMzfVUvG-q4'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://kevin:123456@localhost/flask_db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

class User(db.Model): 
  __tablename__='user'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(40))
  email=db.Column(db.String(40))
  password=db.Column(db.String(40))
 
  def __init__(self,name,email,password):
    self.name=name
    self.email=email
    self.password=password

class UploadFile(db.Model):
  __tablename__='upload'
  id=db.Column(db.Integer,primary_key=True)
  id_user=db.Column(db.Integer, ForeignKey(User.id))
  file_name=db.Column(db.String(120))
  date=db.Column(db.Date)
  file_hash=db.Column(db.String(120))
 
  def __init__(self,id_user,file_name,date,file_hash):
    self.id_user=id_user
    self.file_name=file_name
    self.date=date
    self.file_hash=file_hash

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register-submit', methods = ['POST'])
def register_submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    user = User(name, email, password)
    # db.create_all()
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login-submit', methods = ['POST'])
def login_submit():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter(and_(User.email == email, User.password == password)).first()
    if user:
      session['user_id'] = user.id
      return redirect('/')
    else:
      flash("Gagal login\nEmail atau Password salah")
      return redirect('/login')

@app.route('/')
def home():
    if 'user_id' in session:
      files_data = UploadFile.query.filter_by(id_user=session['user_id'])
      return render_template('upload.html', datas = files_data)
    else:
      return redirect(url_for('login'))
    
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    api = ipfsApi.Client('127.0.0.1', 5001)
    res = api.add(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    file_data = UploadFile.query.filter_by(file_hash=res['Hash']).first()
    if not file_data:
      if 'user_id' in session:
        user = UploadFile(session['user_id'], secure_filename(f.filename), date.today(), res['Hash'])
        db.session.add(user)
        db.session.commit()
      return redirect('/')
    else:
      hash = res['Hash']
      flash(f"{hash} sudah ada")
      return redirect('/')
    
@app.route('/edit-file', methods = ['POST'])
def edit_file():
    id_file = request.args.get('id')
    UploadFile.query.filter(UploadFile.id == id_file).delete()
    db.session.commit()
    return redirect('/')  
  
@app.route('/delete-file')
def delete_file():
    id_file = request.args.get('id')
    UploadFile.query.filter(UploadFile.id == id_file).delete()
    db.session.commit()
    return redirect('/')

@app.route('/pin-file')
def pin_file():
    hash_file = request.args.get('hash')
    api = ipfsApi.Client('127.0.0.1', 5001)
    res = api.pin_add(hash_file)
    return redirect('/')

@app.route('/rm-pin-file')
def rm_pin_file():
    hash_file = request.args.get('hash')
    api = ipfsApi.Client('127.0.0.1', 5001)
    res = api.pin_rm(hash_file)
    return redirect('/')

@app.route('/find')
def find():
    return render_template('find.html')
  
@app.route('/verifier')
def verifier():
    return render_template('verifier.html')

@app.route('/find-ipfs', methods = ['POST'])
def find_to_ipfs():
    fileHash = request.form['text']
    webbrowser.open(f"https://ipfs.io/ipfs/{fileHash}")
    return redirect("/")
  
@app.route('/file-verifier', methods = ['POST'])
def verify_file():
    try:
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      api = ipfsApi.Client('127.0.0.1', 5001)
      res = api.add(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      file_data = UploadFile.query.filter_by(file_hash=res['Hash']).first()
      if not file_data:
        flash(f"file asli tidak ditemukan")  
        return redirect('/verifier')
      else:
        flash(f"file asli terverifikasi")
        return redirect('/verifier')
    except:
      flash(f"something wrong about the file checker")
      return redirect('/verifier')

if __name__ == '__main__':
    app.run(debug=True)
