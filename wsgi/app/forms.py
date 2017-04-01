from flask_wtf import FlaskForm
from wtforms import TextField, validators

class MessageForm(FlaskForm):
	message = TextField(u'What is on your mind?', [validators.optional(), validators.length(max=200)])
