from flask_wtf import FlaskForm
from wtforms import TextField, validators

class MessageForm(FlaskForm):
	message = TextField(u'What is on your mind?', [validators.optional(), validators.length(max=200)])

class ExpenseForm(FlaskForm):
	user_name = TextField(u'User name', [validators.optional(), validators.length(max=20)])
	expense_date = TextField(u'Expense date', [validators.optional(), validators.length(max=20)])
	expense_amount = TextField(u'Expense amount', [validators.optional(), validators.length(max=20)])
	expense_description = TextField(u'Expense description', [validators.optional(), validators.length(max=20)])

