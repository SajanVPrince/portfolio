from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect('D:/Sajan2/portfolio/portfolio/data.db')
try:
    con.execute("create table details(name text,email text,phone text,subject text,message text)")
except:
    pass

# 
# set FLASK_APP=main.py

app=Flask(__name__)

@app.route('/')   #Path of the function
def home():
    return render_template('index.html')

@app.route('/home/')   #Path of the function
def home1():
    return render_template('index.html')