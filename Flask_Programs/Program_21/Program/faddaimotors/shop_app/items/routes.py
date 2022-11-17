from shop_app.admin.routes import category
from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop_app import db, app, photos
from .models import Brand, Category, AddVehiclePart
from .forms import AddVehicleParts
import secrets, os

@app.template_filter()
def numberFormat(value):
    return format(int(value), ',d')

@app.template_filter()
def numberFormatFloat(value):
    return format(float(value), ',')



@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    items = AddVehiclePart.query.filter(AddVehiclePart.stock > 0).order_by(AddVehiclePart.id.desc()).paginate(page=page, per_page=12)
    brands = Brand.query.join(AddVehiclePart, (Brand.id==AddVehiclePart.brand_id)).all()
    categorys = Category.query.join(AddVehiclePart, (Category.id==AddVehiclePart.category_id)).all()
    return render_template('items/home.html', items = items, brands=brands, categorys=categorys, title = 'faddaiMotors - Home')

@app.route('/item/<int:id>')
def view_single_page(id):
    item = AddVehiclePart.query.get_or_404(id)
    brands = Brand.query.join(AddVehiclePart, (Brand.id==AddVehiclePart.brand_id)).all()
    categorys = Category.query.join(AddVehiclePart, (Category.id==AddVehiclePart.category_id)).all()
    return render_template('items/view_single_page.html', item=item, brands=brands, categorys=categorys, title = 'faddaiMotors - View')

@app.route('/brand/<int:id>')
def get_brand(id):
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    page = request.args.get('page', 1, type=int)
    brand = AddVehiclePart.query.filter_by(brand=get_brand).paginate(page=page, per_page=4)
    brands = Brand.query.join(AddVehiclePart, (Brand.id==AddVehiclePart.brand_id)).all()
    categorys = Category.query.join(AddVehiclePart, (Category.id==AddVehiclePart.category_id)).all()
    return render_template('items/home.html', brand=brand, brands=brands, categorys=categorys, get_brand=get_brand)


@app.route('/category/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_category = Category.query.filter_by(id=id).first_or_404()
    get_category_item = AddVehiclePart.query.filter_by(category_id=id).paginate(page=page, per_page=4)
    categorys = Category.query.join(AddVehiclePart, (Category.id==AddVehiclePart.category_id)).all()
    brands = Brand.query.join(AddVehiclePart, (Brand.id==AddVehiclePart.brand_id)).all()
    return render_template('items/home.html', get_category_item=get_category_item, categorys=categorys, brands=brands, get_category=get_category)


@app.route('/addNewbrand', methods=['GET','POST'])
def addNewbrand():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'Brand Name {getbrand} has been added', 'success')
        db.session.commit()
        return redirect(url_for('addNewbrand'))

    return render_template('items/addNewbrand.html', brands = 'brands', title = 'faddaiMotors - Add brand')

@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please go ahead to login first', 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        flash(f"You've updated the brand", 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('items/updatebrand.html', updatebrand=updatebrand, title='faddaiMotors - Update Brand')



@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(brand)
        flash(f'You have successfuly deleted the brand {brand.name}', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f'The brand {brand.name} cannot be deleted', 'warning')
    return redirect(url_for('admin'))



@app.route('/addcategory', methods=['GET','POST'])
def addcategory():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('category')
        category = Category(name=getbrand)
        db.session.add(category)
        flash(f'Category, {getbrand} has been added', 'success')
        db.session.commit()
        return redirect(url_for('addcategory'))

    return render_template('items/addNewbrand.html', title = 'faddaiMotors - Add category')

@app.route('/updatecategory/<int:id>', methods=['GET', 'POST'])
def updatecategory(id):
    if 'email' not in session:
        flash(f'Please go ahead to login', 'danger')
        return redirect(url_for('login'))
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecategory.name = category
        flash(f"You've updated the category", 'success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('items/updatebrand.html', updatecategory=updatecategory, title='faddaiMotors - Update Category')


@app.route('/deletecategory/<int:id>', methods=['POST'])
def deletecategory(id):
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(category)
        db.session.commit()
        flash(f'You have successfuly deleted the brand {category.name}', 'success')
        return redirect(url_for('admin'))
    flash(f'The brand {category.name} cannot be deleted', 'warning')
    return redirect(url_for('admin'))



@app.route('/vehiclePart', methods = ['POST', 'GET'])
def vehiclePart():
    if 'email' not in session:
        flash('Please proceed to login page', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddVehicleParts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        vehiclePart = AddVehiclePart(name=name, price=price, discount=discount, stock=stock, colors=colors,description=description,
         brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(vehiclePart)
        flash(f'The item {name} has been added succesfully', 'success')
        db.session.commit()
        return redirect(url_for('vehiclePart'))
    return render_template('items/additem.html', form=form, brands=brands, categories=categories, title = 'faddaiMotors - Add an item')


@app.route('/updateitem/<int:id>', methods =['GET','POST'])
def updateitem(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    item = AddVehiclePart.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = AddVehicleParts(request.form)
    if request.method == "POST":
        item.name = form.name.data
        item.price = form.price.data
        item.discount = form.discount.data
        item.brand_id = brand
        item.category_id = category
        item.stock = form.stock.data
        item.colors = form.colors.data
        item.description = form.description.data
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_1))
                item.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                item.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_2))
                item.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                item.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_3))
                item.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                item.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")       
        db.session.commit()
        flash(f'The item has been udated successfully', 'success')
        return redirect(url_for('admin'))
    form.name.data = item.name
    form.price.data = item.price
    form.description.data = item.description
    form.stock.data = item.stock
    form.discount.data = item.discount
    form.colors.data = item.colors
    return render_template('items/updateitem.html', form=form, categories=categories, brands=brands, item=item)


@app.route('/deleteitem/<int:id>', methods = ['POST'])
def deleteitem(id):

    item = AddVehiclePart.query.get_or_404(id)
    if request.method == "POST":
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_1))
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_2))
                os.unlink(os.path.join(current_app.root_path, "static/images/" + item.image_3))
            except Exception as messagee:
                print(messagee)
        db.session.delete(item)
        db.session.commit()
        flash(f'The item has been deleted successfully', 'success')      
        return redirect(url_for('admin'))
    flash(f'sorry, this item cannot be deleted', 'danger')
    return redirect(url_for('admin'))