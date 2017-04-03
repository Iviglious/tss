""" Module containing function to operate with the Database """

import os
import pymongo
from datetime import datetime
from flask_pymongo import PyMongo

from app import C_APP


C_APP.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
C_APP.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

MG_DB = PyMongo(C_APP)

# helping functions for the demo
def add_expense(user_name, expense_date, expense_amount, expense_description):
    """ Function to add a new expense to the DB """

    curr_col = MG_DB.db.expenses # it acctually designs a collection called expenses
    result = curr_col.insert_one({'user_name': user_name
                                  , 'expense_date': expense_date
                                  , 'expense_amount': expense_amount
                                  , 'expense_description': expense_description})
    if result:
        return "Expense added successfully! ID={}".format(result.inserted_id)
    else:
        return "Failed to insert the expense!"


def get_all_expenses():
    """ Function to select all expenses from DB """

    all_exp = list()
    for exp in MG_DB.db.expenses.find().sort('expense_date', pymongo.ASCENDING):
        all_exp.append({'user_name': exp['user_name']
                        , 'date':exp['expense_date']
                        , 'amount': exp['expense_amount']})
    return all_exp # save as a list of dictionaries

def get_all_expenses_():
    """ Function to select all expenses from DB """

    return [
        {'user_name':'ivo', 'date':datetime.strptime('2017-03-30', '%Y-%m-%d'), 'amount':1.34}
        , {'user_name':'ivo', 'date':datetime.strptime('2017-03-31', '%Y-%m-%d'), 'amount':4.46}
        , {'user_name':'ivo', 'date':datetime.strptime('2017-04-01', '%Y-%m-%d'), 'amount':6.30}
        , {'user_name':'aline', 'date':datetime.strptime('2017-03-30', '%Y-%m-%d'), 'amount':1.64}
        , {'user_name':'aline', 'date':datetime.strptime('2017-03-31', '%Y-%m-%d'), 'amount':3.78}
        , {'user_name':'aline', 'date':datetime.strptime('2017-04-02', '%Y-%m-%d'), 'amount':2.20}
    ]
