# Reddit Clone
Made in Flask & Python, based on [  
Coding w/ Jake](https://www.youtube.com/channel/UC0np-tFaO8GPJuIKZhwnQxg)

## Project Set Up
In a new dir type `pip3 install virtualenv`
Type `virtualenv ENV` to create a virtual environment named ENV
Type `source ENV/bin/activate` to activate our virtual environment
Install dependencies by typing `pip3 install flask flask-sqlalchemy flask-bcrypt`
Save our requirements by typing `pip3 freeze > requirements.txt`
Create `app.py`
Run `python3 app.py` to run it

## DB Set Up
Go to heroku.com, sign up
Install the heroku CLI by typing `
brew tap heroku/brew && brew install heroku`
In our dir, type `heroku login`
Make our project into a git repo with `git init`
Type `heroku apps:create flask-reddit-kaitlin`
Refresh the heroku dashboard and see `flask-reddit-kaitlin` there now. Click it, click Resources, a credit card on file is required even though it's free..
Under Add-Ons, search for `mysql` and select `ClearDB MySQL` to make our database
Now edit `app.py` to incorporate our DB with SQLAlchemy
Retrieve our connection URL with `heroku config --app flask-reddit-kaitlin` which outputs the following

    CLEARDB_DATABASE_URL: mysql://ba4198534c6b87:6e8ac361@us-cdbr-east-05.cleardb.net/heroku_96b6ad4b9cb7eec?reconnect=true

The lines in app.py associated with this are



       app.config['SQLAlchemy_DATABASE-URI'] = 'mysql://ba4198534c6b87:6e8ac361@us-cdbr-east-05.cleardb.net/heroku_96b6ad4b9cb7eec'
       db = SQLAlchemy(app)

Now, let's set up our User Model. Here's the code in app.py

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

Oops! We forgot a dependency!
`pip3 install mysqlclient`
Save our requirements by typing `pip3 freeze > requirements.txt`

In dir, type
`python3`
`from app import db`
`db.create_all()`

No errors! `exit()`
Our User table has now been created in our database

##  Templates
Create dir `templates`

In app.py, edit our route to add `render_template`

    @app.route('/')
    def index():
        return render_template('index.html')

Then create `index.html` in `templates`

Now to make our job easier in creating the layout, we'll use template inheritance. Create `base.html` in `templates`

Use Jinja 2 (the template engine that Flask uses) syntax like `{% %}`
Add `  {% block head %}
        {% endblock %}`

Go to `index.html` and add `{% extends 'base.html' %}` to implement template inheritance

## Static Content
Create a dir called `static` and in that create `style.css`

In your desired html file, type

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
 This syntax is important !!! Inside the `{{ }}` is Python and the double brackets mean to convert the contents to a str

 ## Adding Bootstrap 4
 Go to getbootstrap.com or https://getbootstrap.com/docs/5.1/getting-started/introduction/

Add the css & JS html tags to `base.html` **below** the blocks

We're going to replace our `static` dir and the reference to it in `index.html` because we're going to be using Bootstrap instead

Remember to be in your virtual environment. If you're not, `source ENV/bin/activate`. If for some reason you need to get out of venv, `deactivate`

Bug -- icons are funky
