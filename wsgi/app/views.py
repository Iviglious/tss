""" Module for handling the main route directives """

from flask import render_template
#import unirest

#from forms import MessageForm, ExpenseForm
from app import C_APP


@C_APP.route('/')
@C_APP.route('/index/')
def index():
    """Routing function for index"""

    return render_template("index.html")

