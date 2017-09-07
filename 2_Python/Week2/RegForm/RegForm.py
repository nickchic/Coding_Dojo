from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
DATE_REGEX = re.compile(r'^\d{1,2}\/\d{1,2}\/\d{4}$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def display_results():
    print "Results page loaded", session['name'], session['language'], session['dojo'], session['comment']
    return render_template('results.html', name=session['name'], dojo=session['dojo'], language=session['language'], comment=session['comment'])

@app.route('/action', methods=['POST'])
def submit_form():

    print "Form Submitted", request.form['name'], request.form['email'], request.form['password'], request.form['confirm'], request.form['dob']
    form_complete = True
    #checks if name is blank
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
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



    if len(request.form['dob']) < 1:
        flash("DOB must not be blank")
        form_complete = False
    elif not DATE_REGEX.match(request.form['dob']):
        flash("DOB must be in date form (MM/DD/YYYY)")
        form_complete = False
    else:
        dateToCheck = datetime.datetime.strptime(request.form['dob'], "%m/%d/%Y")
        if dateToCheck.date() < datetime.today().date():
            flash("Were you born in the future?")
            form_complete = False

    if form_complete:
        #stores values
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm'] = request.form['confirm']
        print "Data Stored", session['name'], session['email'], session['password'], session['confirm']
        return redirect('/complete')
    else:
        return redirect('/')

@app.route('/complete')
def complete():
    return render_template('complete.html')

app.run(debug=True)
