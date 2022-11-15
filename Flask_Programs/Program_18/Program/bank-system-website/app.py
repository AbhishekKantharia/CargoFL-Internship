from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets
from flask_migrate import Migrate, migrate


# flask app
app = Flask(__name__)

# configure database 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@172.23.66.230/bankSystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ujvfyztmpflqtf:4a6caeb248b5cbc98dcdbcfb061d38eeaa481f1bd1499cd78a2732f4d295b8e6@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/d9m27o98jihovf'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app secrete keyframework
secret = secrets.token_urlsafe(32)
app.secret_key = secret

# basic model
class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    currentBalance = db.Column(db.String(20), nullable=False)
    accountNo = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(45), nullable=False)


class Transecetion(db.Model):
    __tablename__ = 'transection'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    transferFrom = db.Column(db.String(45), nullable=False)
    transferTo = db.Column(db.String(45), nullable=False)
    amount = db.Column(db.String(45), nullable=False)
    time = db.Column(db.String(45), nullable=False)



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/customer")
def customer(msg=""):
    data = Customer.query.filter().all()
    return render_template('customer.html',data=data,msg=msg)

@app.route("/transfer/<string:page_id>", methods=['POST','GET'])
def transfer(page_id):
    if request.method == 'GET':
        customer_data = Customer.query.filter().all()
        page_data = Customer.query.filter_by(id=page_id)
        return render_template('transfer.html',data=page_data,customers=customer_data)

    if request.method == 'POST':
        name_from = request.form.get('transferFrom')
        name_to = request.form.get('transferTo')
        amount = request.form.get('amount')
        if len(name_to) != 0 and len(amount) != 0:
            sender = Customer.query.filter_by(name=name_from).first()
            if float(sender.currentBalance) > float(amount):
                receiver = Customer.query.filter_by(name=name_to).first()
                sender.currentBalance = float(sender.currentBalance) - float(amount)
                receiver.currentBalance = float(receiver.currentBalance) + float(amount)
                entry = Transecetion(transferFrom=name_from,transferTo=name_to,amount=amount,time=datetime.now())
                db.session.add(entry)
                db.session.commit()
                msg = "Transfer Successful."
            else:
                msg = "Transfer Error!"
        return transecetion(msg)
    

@app.route('/transecetion')
def transecetion(msg=""):
    tr_data = Transecetion.query.filter().all()
    return render_template('transecetion.html',data=tr_data,msg=msg)

@app.route('/create',methods=["POST","GET"])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        customer_data = Customer.query.filter().all()
        last_value = customer_data[-1]
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        amount = request.form.get('balance')
        acountNo = last_value.accountNo + 1
        entry = Customer(name = name,email = email, phone = phone, currentBalance=amount,accountNo=acountNo,time=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return customer(msg="Account create Successfull!")



if __name__=="__main__":
	db.create_all()
	app.run(debug=True)