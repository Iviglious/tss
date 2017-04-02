""" Module for demostrating DB operations """

import os
import datetime
from flask_pymongo import PyMongo
from flask import jsonify

from app import C_APP


C_APP.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
C_APP.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

MG_DB = PyMongo(C_APP)

@C_APP.route('/demo_db')
def demo_db():
    """ Function to list the DB's """

    return jsonify({'result': MG_DB.db.collection_names()})

@C_APP.route('/demo_db/add')
def db_add():
    """ Function to add rows """

    sample_expense = {
        'user_name':'ivo'
        , 'expense_date': datetime.datetime.now()
        , 'expense_amount': 13.95
        , 'expense_description': 'Sample expense as a start.'
    } # sample value

    curr_col = MG_DB.db.expenses # it acctually designs a collection called expenses
    result = curr_col.insert_one(sample_expense)
    if result:
        return "Expense inserted successfully! ID={}".format(result.inserted_id)
    else:
        return "Failed to insert the expense!"

@C_APP.route('/demo_db/expenses')
def show_all_expenses():
    """ Function to list all the expenses """

    return jsonify({'expenses': MG_DB.db.expenses.find()})
