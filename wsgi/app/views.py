from app import app

@app.route('/')
@app.route('/index')

def index():
	return "<center><h1>Welcome to Family Budget</h1></center>"

