""" Module containing function to operate with the Database """

import os
import pymongo
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

def get_all_expenses_():
    """ Function to select all expenses from DB """

    return None

def get_all_expenses():
    """ Function to select all expenses from DB """

    all_exp = list()
    for exp in MG_DB.db.expenses.find().sort('expense_date', pymongo.ASCENDING):
        all_exp.append({'user_name': exp['user_name']
                        , 'date':"{:%Y-%m-%d %H:%M}".format(exp['expense_date'])
                        , 'amount': "{:.2f}".format(exp['expense_amount'])})
    return all_exp # save as a list of dictionaries

