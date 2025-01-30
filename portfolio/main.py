from flask import Flask,render_template,request

# set FLASK_APP=main.py

app=Flask(__name__)

@app.route('/')   #Path of the function
def home():
    return render_template('index.html')

@app.route('/home/')   #Path of the function
def home1():
    return render_template('index.html')

app.run(debug=True)