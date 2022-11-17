from typing import Dict
from shop_app.items.routes import vehiclePart
from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop_app import db, app
from shop_app.items.models import AddVehiclePart


def MergeDicts(dict1, dict2):
    if isinstance(dict, list) and isinstance(dict1, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False




@app.route('/AddtoBag', methods = ['POST'])
def AddtoBag():
    try:
        item_id = request.form.get('item_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        vehiclePart = AddVehiclePart.query.filter_by(id=item_id).first()
        if item_id and colors and quantity and request.method == "POST":
            DictVehicleParts = {
                item_id: {'name': vehiclePart.name, 'price': vehiclePart.price, 
                'discount': vehiclePart.discount, 'color': colors, 
                          'quantity': quantity, 'image': vehiclePart.image_1, 'colors': vehiclePart.colors
                }
            }

            if 'ShoppingBag' in session:
                print(session['ShoppingBag'])
                if item_id in session['ShoppingBag']:
                    print("This item is already in Bag")
                else:
                    session['ShoppingBag'] = MergeDicts(session['ShoppingBag'], DictVehicleParts)
                    return redirect(request.referrer)


            else:
                session['ShoppingBag'] = DictVehicleParts
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/bagItems')
def getBag():
    if 'ShoppingBag' not in session:
        return redirect(request.referrer)
    total = 0
    grandTotal = 0
    for key, item in session['ShoppingBag'].items():
        discount = (item['discount']/100) * float(item['price'])
        total += float(item['price']) * int(item['quantity'])
        total -= discount
        tax = ("%.2f" % (.06 * float(total)))
        grandTotal = float("%.2f" % (1.06 * total))
    return render_template('items/bag.html', tax = tax, grandTotal = grandTotal)


@app.route('/empty')
def empty_bag():
    try:
        session.clear()
        return redirect(url_for('home'))
    except Exception as e:
        print(e)


@app.route('/updatebag/<int:code>', methods=['POST'])
def updatebag(code):
    if 'ShoppingBag' not in session and len(session['ShoppingBag']) <= 0:
        return redirect(url_for('home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        color = request.form.get('color')
        try:
            session.modified = True
            for key, item in session['ShoppingBag'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    flash('Item has been Updated!')
                    return redirect(url_for('getBag'))
        except Exception as e:
            print(e)
            return redirect(url_for('getBag'))
