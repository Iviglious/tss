""" Module for initialization of the app """

import os
from flask import Flask

C_APP = Flask(__name__)
C_APP.secret_key = os.environ['APP_SECRET_KEY']

from app import views
