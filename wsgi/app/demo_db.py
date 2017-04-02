""" Module for demostrating DB operations """

import os
from flask_pymongo import PyMongo
from flask import jsonify

from app import C_APP


C_APP.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
C_APP.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

#MG_DB = PyMongo(C_APP)

@C_APP.route('/demo_db')
def demo_db():
    """ Function to list the DB's """

    return jsonify({'result': C_APP.config['MONGO_URI']})
    #return jsonify({'result': MG_DB.db.collection_names()})
