from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'rest')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import datetime
import time
now = time.time()
st = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/users')
def index():
    #Displays all users
    users = mysql.query_db("SELECT * FROM users")
    return render_template('users.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    #Form submission that adds new user
    new_user_query = "INSERT INTO `rest`.`users` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', NOW(), NOW() );".format(request.form['first_name'], request.form['last_name'],request.form['email'])
    mysql.query_db(new_user_query)
    return redirect('/users')


@app.route('/edit_user', methods=['POST'])
def edit_user():
    #Form submission that edits new user
    update_query = "UPDATE `rest`.`users` SET `first_name`='{}',`last_name`='{}', `email`='{}', `updated_at`= NOW() WHERE `id`='{}';".format(request.form['first_name'], request.form['last_name'], request.form['email'], request.form['id'],)
    mysql.query_db(update_query)
    return redirect('/users')

@app.route('/users/<id>')
def user_page(id):
    #Brings up the edit user page
    user_query = "SELECT * FROM users WHERE id = {}".format(str(id))
    user = mysql.query_db(user_query)
    return render_template('user.html', user=user[0])

@app.route('/users/new')
def new_user_page():
    #Brings up the add new user page
    return render_template('add_user.html')


@app.route('/users/<id>/edit')
def edit_user_page(id):
    #Brings up the edit user page
    user_query = "SELECT * FROM users WHERE id = {}".format(str(id))
    user = mysql.query_db(user_query)
    return render_template('edit_user.html', user=user[0])


@app.route('/users/<id>/destroy')
def destroy_user_page(id):
    #Deletes user
    delete_query = "DELETE FROM `rest`.`users` WHERE `id`='{}';".format(str(id))
    mysql.query_db(delete_query)
    return redirect('/users')



app.run(debug=True)
