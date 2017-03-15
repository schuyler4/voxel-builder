from flask import Flask, request, render_template
from auth import auth
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = './data.db'
Base = declarative_base()
app.register_blueprint(auth)

@app.route('/')
def builder():
    return  render_template('index.html', title = 'Projects')

if __name__ == "__main__":
    app.run(debug=True)
