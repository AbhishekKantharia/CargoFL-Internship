from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


class MyForm(FlaskForm):
    name = StringField(label='email', validators=[DataRequired(),Email("please enter a valid email")])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8, message="Length is at least 8 characters!")])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.name.data)
        if (form.name.data == "admin@gmail.com") and (form.password.data =="12345678"):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)