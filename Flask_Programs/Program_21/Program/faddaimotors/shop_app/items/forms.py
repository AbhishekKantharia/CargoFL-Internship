from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, BooleanField,DecimalField, TextAreaField, validators
from wtforms.form import Form
from wtforms.validators import InputRequired

class AddVehicleParts(Form):
    name = StringField('Name', [InputRequired()])
    price = DecimalField('Price', [InputRequired()])
    discount = IntegerField('Discount', default = 0)
    stock = IntegerField('Stock', [InputRequired()])
    description = TextAreaField('Description', [InputRequired()])
    colors = TextAreaField('Colors', [InputRequired()])


    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg','png','gif','jpeg'])])