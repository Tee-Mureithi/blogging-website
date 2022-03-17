from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
#from flask_wtf import import Required
#from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    text = TextAreaField('Text')
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:')
    submit = SubmitField('Submit')
