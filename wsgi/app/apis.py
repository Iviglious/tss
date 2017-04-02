""" Module for handling the routes directed for APIs"""

from flask import render_template, request, jsonify
import unirest

from app.forms import MessageForm
from app import C_APP

@C_APP.route('/api/1.0/expenses')
def get_expenses():
    """ Handling API v1.0 expenses route """

    expenses_arr = [
        {'id':1, 'type':'Other', 'amount':1.34}
        , {'id':2, 'type':'Other', 'amount':5.10}
    ]
    return jsonify({'expenses':expenses_arr})


@C_APP.route('/emotion/')
def emotion():
    """ Handle the emotion (GET) """

    return render_template("my_form.html", mood='Question', form=MessageForm())

@C_APP.route('/emotion/', methods=['POST'])
def emotion_post():
    """ Handles the emotion (POST) """

    msg = request.form['message']
    response = unirest.post("https://community-sentiment.p.mashape.com/text/",
                            headers={
                                "X-Mashape-Key":"6VWQcE5umumsh9oLsHfFlOseFGbDp1caaUKjsnj6PJRqxZKslv"
                                                , "Content-Type":"application/x-www-form-urlencoded"
                                                                 , "Accept":"application/json"
                            },
                            params={
                                "txt": msg
                            }
                           )
    return render_template("my_form.html"
                           , mood=response.body['result']['sentiment']
                           , form=MessageForm()
                          )
