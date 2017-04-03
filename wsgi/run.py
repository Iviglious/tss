""" Module for executing the local server """

from werkzeug.contrib.fixers import ProxyFix

from app import C_APP

C_APP.wsgi_app = ProxyFix(C_APP.wsgi_app)

if __name__ == "__main__":
    C_APP.run(debug=False)

