""" Module for initialization of the app """

from flask import Flask

C_APP = Flask(__name__)
C_APP.secret_key = 'Iviglious is awesome!'

from app import views, demo, apis
