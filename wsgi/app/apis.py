""" Module for handling the routes directed for APIs"""

import os
from flask import render_template, request, jsonify
#from bson.json_util import dumps
import unirest

from app.forms import MessageForm
from app import C_APP
from app.DB import MG_DB


@C_APP.route('/api/1.0/expenses')
def get_expenses():
    """ Handling API v1.0 expenses route """

    #expenses_arr = [
    #    {'id':1, 'type':'Other', 'amount':1.34}
    #    , {'id':2, 'type':'Other', 'amount':5.10}
    #]

    #expenses_arr = MG_DB.db.expenses.find()
    #return jsonify({'expenses':expenses_arr})
    return jsonify({'expenses':MG_DB.db.get_all_expenses()})

    # Show all expenses as json
    #return dumps(MG_DB.db.expenses.find())


@C_APP.route('/emotion/')
def emotion():
    """ Handle the emotion (GET) """

    return render_template("emoti_api.html", mood='Question', form=MessageForm())

@C_APP.route('/emotion/', methods=['POST'])
def emotion_post():
    """ Handles the emotion (POST) """

    msg = request.form['message']
    response = unirest.post(os.environ['APP_A_URL'],
                            headers={
                                "X-Mashape-Key":os.environ['APP_A_KEY']
                                                , "Content-Type":"application/x-www-form-urlencoded"
                                                                 , "Accept":"application/json"
                            },
                            params={
                                "txt": msg
                            }
                           )
    return render_template("emoti_api.html"
                           , mood=response.body['result']['sentiment']
                           , form=MessageForm()
                          )
