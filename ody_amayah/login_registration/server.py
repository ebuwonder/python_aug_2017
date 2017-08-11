from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii


app = Flask(__name__)
app.secret_key = 'thesecretkey'

mysql = MySQLConnector(app,'loginreg')

@app.route('/')
def home():
  return redirect('/users/new')

@app.route('/users/new')
def users_new():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    is_valid = True

    if first_name == '':
        is_valid = False
        flash('Name cannot be blank.')
    if last_name == '':
        is_valid = False
        flash('Name cannot be blank.')
    if email == '':
        is_valid = False
        flash('Email cannot be blank.')
    if len(password) < 4:
        is_valid = False
        flash('Password must be at least four characters')
    if password != password_confirmation:
        is_valid = False
        flash('Passwords do not match')

    if is_valid == True:

        salt = binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()
        print hashed_pw

        query = 'insert into users (first_name, last_name, email, password, salt, created_at, updated_at) values (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())'
        data = {
              'first_name':first_name,
              'last_name':last_name,
              'email':email,
              'password':hashed_pw,
              'salt': salt
        }

        user_id = mysql.query_db(query,data)
        session['user_id'] = user_id
        session['is_logged_in'] = True
        return redirect('/success')
    else:
        return redirect('/users/new')

@app.route('/success')
def success():
    return render_template('success.html', session=session)

@app.route('/users/login', methods=['POST'])
def login():
    query = 'select * from users where email= :email'
    data = {'email': request.form['email']}
    user = mysql.query_db(query, data)

    if len(user)== 0:
        flash('Invalid credentials')
        return redirect('/users/new')
    else:
        hashed_input_password = md5.new(request.form['password'] + user[0]['salt']).hexdigest()
        if len(user) !=0 and hashed_input_password == user[0]['password']:
            session['user_id']= user[0]['id']
            session['is_logged_in'] = True
            return redirect('/success')
        else:
            flash('Invalid credentials')
            return redirect('/users/new')

@app.route('/users/logout', methods=['POST'])
def logout():
    session['user_id'] = None
    session['is_logged_in'] = False
    return redirect('/users/new')



app.run(debug=True)
