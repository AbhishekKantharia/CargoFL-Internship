# IPFS Simple Web App

### Overview
Simple website application for storing files in IPFS using flask and posgresql.

### Setup
```sh
  # clone repository 
  $ git clone https://github.com/MohFahmi27/IPFS-Flask-Web-Simple.git
  # generate virtual environment.
  $ python -m venv venv
  # activate virtual environment
  $ venv/Scripts/activate
  # install packages
  $ (venv) pip install -r requirements.txt
```

### How to
Running website in local steps:
1. Create database using postgresql with name flask_db
2. Before running the website you must already installed [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/) 
2. change the app.config['SQLALCHEMY_DATABASE_URI'] value

```sh
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{Your User}:{Password User}@localhost/flask_db'
```

4. Run the app.py

```sh
  $ (venv) python app.py
```

### License
```
MIT License

Copyright (c) 2022 Mohammad Fahmi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
