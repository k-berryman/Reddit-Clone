from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE-URI'] = 'mysql://ba4198534c6b87:6e8ac361@us-cdbr-east-05.cleardb.net/heroku_96b6ad4b9cb7eec'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello worlddd'

if __name__ == '__main__':
    app.run(debug=True)
