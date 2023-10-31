from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,validators,FileField

class CategoryForm(FlaskForm):
    name = StringField('name', [validators.DataRequired()])
    description = TextAreaField('description', [validators.DataRequired()])
    image = FileField('Image', [validators.DataRequired()])