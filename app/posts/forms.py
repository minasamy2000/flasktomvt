from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,validators,FileField

class PostForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    body = TextAreaField('Body', [validators.DataRequired()])
    image = FileField('Image', [validators.DataRequired()])
    