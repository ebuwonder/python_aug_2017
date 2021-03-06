from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'sakila')

@app.route('/')
@app.route('/')
def index():
    query = "SELECT * FROM customers"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html') # pass data to our template

@app.route('/customers', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
    
app.run(debug=True)
