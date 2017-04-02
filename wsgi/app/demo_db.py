""" Module for demostrating DB operations """

import os
import datetime
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps

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
        , 'expense_amount': 4.36
        , 'expense_description': 'This is really working!'
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

    #all_exp = dumps(MG_DB.db.expenses.find())
    #return all_exp # return all as json

    # save as a HTML table
    html_str = "<table>"
    html_str += "<tr>"
    html_str += "<th>user_name</th>"
    html_str += "<th>expense_date</th>"
    html_str += "<th>expense_amount</th>"
    html_str += "<th>expense_description</th>"
    html_str += "</tr>"

    for exp in MG_DB.db.expenses.find():
        html_str += "<tr>"
        html_str += "<td>{}</td>".format(exp['user_name'])
        html_str += "<td>{}</td>".format(exp['expense_date']['$date'])
        html_str += "<td>{}</td>".format(exp['expense_amount'])
        html_str += "<td>{}</td>".format(exp['expense_description'])
        html_str += "</tr>"
    html_str += "</table>"
    return html_str

