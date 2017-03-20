from flask import Flask, render_template, session, g
from auth import auth_blueprint
from builder import builder_blueprint
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = './data.db'
app.register_blueprint(auth_blueprint)
app.register_blueprint(builder_blueprint)
app.secret_key = 'fsaldkfj809fds800fs008098'


@app.route('/')
def start():
    return render_template('start.html')

@app.errorhandler(404)
def pageNotFound(error):
	return "404 page not found"

@app.errorhandler(500)
def internal_error(error):
    return "500 server error"

if __name__ == "__main__":
    app.run(debug=True)
