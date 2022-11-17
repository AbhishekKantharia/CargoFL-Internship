from wtforms import form
from shop_app.items.forms import AddVehicleParts
from flask import Flask, render_template, session, request, flash, url_for, redirect


from shop_app import app, bcrypt, db, items
from .models import User
from .forms import RegistrationForm, LoginForm
from shop_app.items.models import  AddVehiclePart, Brand, Category


#app = Flask(__name__) 


@app.template_filter()
def numberFormat(value):
    return format(int(value), ',d')


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    items = AddVehiclePart.query.all()
    return render_template('admin/index.html', items=items, title = 'Admin')

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title ='Brands', brands=brands)


@app.route('/category')
def category():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title ='Categories', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f' Welcome on board, {form.username.data}. Now login' , 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form = form, title = 'faddaiMotors - Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f"Welcome Back {form.email.data}, you're logged in", 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Incorect email or password, try again', 'danger')
    return render_template('admin/login.html', form = form, title = 'faddaiMotors - Login')


if __name__ == '__main__':
    app.run(port=7000, debug=True)
