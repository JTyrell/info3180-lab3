from flask_wtf import FlaskForm
from wtforms import Form,StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = TextAreaField('Name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    
    email = TextAreaField('Email',
                        validators=[DataRequired(),Email()])
    
    subject = TextAreaField('Subject',
                          validators=[DataRequired(), Length(min=2, max=200)])
    
    msgbody = TextAreaField('Message',
                          validators=[DataRequired(), Length(min=2, max=10000)])

    send = SubmitField('Send')
