from flask import Flask, request, render_template
from auth import auth
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = './data.db'
app.register_blueprint(auth)
app.secret_key = 'fsaldkfj809fds800fs008098'


@app.route('/')
def builder():
    return  render_template('builder.html', title = 'Projects')


if __name__ == "__main__":
    app.run(debug=True)
