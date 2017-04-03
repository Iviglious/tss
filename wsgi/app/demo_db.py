""" Module for demostrating DB operations """

import datetime
from flask import jsonify
#from bson.json_util import dumps

from app import C_APP
from app.DB import MG_DB


@C_APP.route('/demo_db')
def demo_db():
    """ Function to list the DB's """

    return jsonify({'result': MG_DB.db.collection_names()})

@C_APP.route('/demo_db/add')
def db_add():
    """ Function to add rows """

    sample_expense = {
        'user_name': u'ivo'
        , 'expense_date': datetime.datetime.utcnow() # utc time
        , 'expense_amount': 1.63
        , 'expense_description': u'And now another expense!'
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
    html_str += "<th>id</th>"
    html_str += "</tr>"

    for exp in MG_DB.db.expenses.find():
        html_str += "<tr>"
        html_str += "<td>{}</td>".format(exp['user_name'])
        html_str += "<td>{:%Y-%m-%d %H:%M} {}</td>".format(exp['expense_date'], type(exp['expense_date']))
        html_str += "<td>{} {}</td>".format(exp['expense_amount'], type(exp['expense_amount']))
        html_str += "<td>{}</td>".format(exp['expense_description'])
        html_str += "<td>{}</td>".format(exp['id'])
        html_str += "</tr>"
    html_str += "</table>"
    return html_str


@C_APP.route('/demo_db/remove/<row_id>')
def remove_row(row_id):
    """ Function for removal of row from expenses collection """

    res = MG_DB.db.expenses.delete_one(row_id)
    return "Number of rows removed: {}<br><br>\
    View all <a href='/demo_db/expenses'>expenses</a>".format(res.deleted_count)
