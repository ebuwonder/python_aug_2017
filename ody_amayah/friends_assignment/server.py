from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')

@app.route('/')
def index():
    query = 'select * from friends'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)


@app.route('/friends', methods=['POST'])
def Create():
    query = 'insert into friends(name, age, created_at, updated_at) values(:name, :age, now(), now())'
    data = {
          'name' : request.form['name'],
          'age' : request.form['age'],
    }
    mysql.query_db(query,data)
    return redirect('/')
app.run(debug=True)
