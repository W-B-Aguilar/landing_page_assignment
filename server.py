from flask import Flask, render_template, redirect, request
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninjas')
def info():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo_news():
   print "Got Post Info"
#    name = request.form['name']
#    email = request.form['email']
   return render_template('dojos.html')




app.run(debug=True)