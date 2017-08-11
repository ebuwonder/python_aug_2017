from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    query = 'select * from emails'
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails = emails)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/', methods=['POST'])
def Create():
    query = 'insert into emails(address created_at, updated_at) values(:address, now(), now())'
    data = {'address' : request.form['address']}
    mysql.query_db(query,data)
    return redirect('success.html')
app.run(debug=True)
