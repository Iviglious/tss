from app import app
from flask import render_template, request, jsonify
import unirest
from forms import MessageForm, ExpenseForm

@app.route('/api/1.0/expenses')
def get_expenses():
	expenses_arr =[
			 {'id':1, 'type':'Other','amount':1.34}
			,{'id':2, 'type':'Other','amount':5.10}
		]
	return jsonify({'expenses':expenses_arr})


@app.route('/emotion/')
def emotion():
	return render_template("my_form.html", mood='Question', form=MessageForm())

@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
		headers={
			"X-Mashape-Key": "6VWQcE5umumsh9oLsHfFlOseFGbDp1caaUKjsnj6PJRqxZKslv",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "application/json"
    			},
		params={
			"txt": msg
			}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())
