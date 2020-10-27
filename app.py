import os

from flask import Flask, render_template, request, g, redirect, url_for
from peewee import SqliteDatabase

from models import create_tables
from helpers import get_all_tasks, create_task


DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret-key')
DB_NAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tasks.db')


app = Flask(__name__)
app.config.from_object(__name__)
database = SqliteDatabase(DB_NAME)

create_tables(database)  # Create DB

# Middlewares
@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


# Routes
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        create_task(name)

        return redirect(url_for('index'))
    else:
        return render_template('add.html')


@app.route('/', methods=['GET'])
def index():
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)
