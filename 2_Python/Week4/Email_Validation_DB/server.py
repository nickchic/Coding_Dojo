from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'test_users')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def email():
    form_complete = True
    #checks that the form is filled and is a valid email
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        form_complete = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email not valid")
        form_complete = False

    if form_complete:
        #adds email to data base and loads the success page
        query = "INSERT INTO users (email, created_at) VALUES (:email, NOW())"
        data = {
                 'email': request.form['email']
               }
        mysql.query_db(query, data)
        flash(request.form['email'])
        return redirect('/success')
    else:
        return redirect('/')



@app.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM users")
    return render_template('success.html', emails=emails)


app.run(debug=True)
