""" Module for defining the forms used in the app """

from flask_wtf import FlaskForm
from wtforms import TextField, validators

class MessageForm(FlaskForm):
    """ Form Class for the emotion API """

    message = TextField(u'What is on your mind?'
                        , [validators.optional(), validators.length(max=200)]
                       )

class ExpenseForm(FlaskForm):
    """ Form class for the expenses """

    user_name = TextField(u'User name'
                          , [validators.optional(), validators.length(max=20)])
    expense_date = TextField(u'Expense date'
                             , [validators.optional(), validators.length(max=20)])
    expense_amount = TextField(u'Expense amount'
                               , [validators.optional(), validators.length(max=20)])
    expense_description = TextField(u'Expense description'
                                    , [validators.optional(), validators.length(max=20)])

