from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
#from flask_wtf import import Required
#from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField('Blog title')
    text = TextAreaField('Text')
    category = SelectField('Type',choices=[('lifestyle','LIfestyle blog'),('motivation','Motivation blog'),('mentalhealth','Mentalhealth blog')])


    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:')
    submit = SubmitField('Submit')
