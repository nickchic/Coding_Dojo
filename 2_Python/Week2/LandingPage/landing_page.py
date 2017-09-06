from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo():
    return render_template('dojo.html')

@app.route('/action', methods=['POST'])
def named_dojo():
    name = request.form['name']
    print "Form Submited", name
    return redirect('/')

app.run(debug=True)
