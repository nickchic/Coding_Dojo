from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'wall')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import datetime
import time
now = time.time()
st = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    try:
        session['id']
    except:
        session['id'] = -1

    users = mysql.query_db("SELECT * FROM users")
    print users

    if session['id'] == -1:
        return render_template('login.html', logged_in=False)
    else:
        user_query = "SELECT * FROM users WHERE id = :id"
        user_data = {'id':session['id']}
        logged_in_user = mysql.query_db(user_query, user_data)
        return render_template('login.html', name=logged_in_user[0]['first_name'] ,logged_in=True)


@app.route('/reg', methods=['POST'])
def register():
    print request.form['first_name'], request.form['last_name'], request.form['email'], request.form['password'], request.form['confirm']

    form_complete = True

    #checks if first name is blank
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank")
        form_complete = False
    elif not request.form['first_name'].isalpha():
        flash("Last name cannot have numbers")
        form_complete = False

    #checks if last name is blank
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank")
        form_complete = False
    elif not request.form['last_name'].isalpha():
        flash("Last name cannot have numbers")
        form_complete = False

    #checks if email is blank then if its in the right format
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        form_complete = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email not valid")
        form_complete = False

    #checks if password is blank or the right length
    if len(request.form['password']) < 1:
        flash("Password cannot be blank")
        form_complete = False
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        form_complete = False
    elif request.form['password'].islower() or request.form['password'].isalpha():
        flash("Password must have a capital and a number")
        form_complete = False

    #checks if passwords match
    if not request.form['confirm'] == request.form['password']:
        flash("Confirm Password does not match")
        form_complete = False

    if form_complete:
        print "form good"
        #hashes password
        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        #enters data into database
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'password': pw_hash
               }

        mysql.query_db(query, data)

        #gets id number from database and stores it, logging in the user
        id_query = "SELECT MAX(id) AS id FROM users"
        id = mysql.query_db(id_query)
        session['id'] = id[0]['id'];
        print session['id']
        return redirect('/wall')

    else:
        print "form bad"
        return redirect('/')


@app.route('/wall')
def wall():

    # Accesses users information to display their name
    user_query = "SELECT * FROM users WHERE id = :id"
    user_data = {'id':session['id']}
    logged_in_user = mysql.query_db(user_query, user_data)
    print "id = " + str(session['id'])

    #Gets posts data
    wall_query = "SELECT first_name, last_name, message, messages.created_at AS created_at, messages.id AS message_id, users.id AS user_id FROM messages LEFT JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    wall_posts = mysql.query_db(wall_query)

    #Gets comment data by taking id's from messages query above and making that the key in a dictionary. each key in dictionary is a list of comments for that message
    comment_data = {}
    for message in wall_posts:
        comment_query = "SELECT first_name, last_name, comment, comments.created_at AS created_at, comments.message_id as message_id FROM comments LEFT JOIN users ON comments.user_id = users.id WHERE comments.message_id = %s ORDER BY comments.created_at" %(message['message_id'])
        print comment_query
        comment_data[message['message_id']] = (mysql.query_db(comment_query))

    print comment_data

    return render_template('wall.html', logged_in_user=logged_in_user[0], posts=wall_posts, comments=comment_data)


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/login_attempt', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['id'] = user[0]['id'];
        return redirect('/wall')
    else:
        flash("Incorrect Log In")
        return redirect('/')

@app.route('/wall_post', methods=['POST'])
def wall_post():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
             'user_id': session['id'],
             'message': request.form['message'],
           }
    mysql.query_db(query, data)
    print request.form['message']
    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    comment_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    comment_data = {
             'user_id': session['id'],
             'message_id': message_id,
             'comment': request.form['comment'],
           }
    mysql.query_db(comment_query, comment_data)
    return redirect('/wall')

@app.route('/deletepost/<post_id>', methods=['POST'])
def delete_post(post_id):
    delete_post_query = "DELETE FROM messages WHERE id = " + str(post_id)
    mysql.query_db(delete_post_query)
    return redirect('/wall')

app.run(debug=True)
