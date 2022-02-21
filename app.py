from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Set up Flask app
app = Flask(__name__)

# Set up and connect to Heroku Database
app.config['SQLAlchemy_DATABASE-URI'] = 'mysql://ba4198534c6b87:6e8ac361@us-cdbr-east-05.cleardb.net/heroku_96b6ad4b9cb7eec'
db = SQLAlchemy(app)

# Set up User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Username can be up to 100 chars & cannot be blank & has to be a new username
    username = db.Column(db.String(100), nullable=False, unique=True)
    # Email can be up to 120 chars & cannot be blank & has to be a new username
    email = db.Column(db.String(120), nullable=False, unique=True)
    # Password can be up to 120 chars & cannot be blank
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
