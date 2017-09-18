from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'mydb')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    try:
        session['id']
    except:
        session['id'] = -1
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('index.html')


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
        return redirect('/success')

    else:
        print "form bad"
        return redirect('/')


@app.route('/success')
def success():
    user_query = "SELECT * FROM users WHERE id = :id"
    user_data = {'id':session['id']}
    logged_in_user = mysql.query_db(user_query, user_data)
    print "id = " + str(session['id'])
    return render_template('success.html', name=logged_in_user[0]['first_name'])


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
        return redirect('/success')
    else:
        flash("Incorrect Log In")
        return redirect('/')


app.run(debug=True)
