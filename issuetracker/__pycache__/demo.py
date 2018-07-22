from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'

'''
Username
FirstName
LastName
Password
AccessToken'''
user_details = [{'Username' : 'Mohit01' , 'FirstName': 'Mohit' , 'LastName': 'Atul', 'Password': 'asdsd', 'AccessToken': '2xg'},
{'Username' : 'Rohit16' , 'FirstName': 'Rohit' , 'LastName': 'Garg', 'Password': 'asdss', 'AccessToken': '2xj'}
]

'''
Title
Description
AssignedTo (User relation)
Createdby (User relation)
Status (Open, Closed)
'''

issue_details = [{'Title': 'problem 1', 'Description': 'afas', 'AssignedTo': 'person 1','Createdby':'Mohit01', 'Status': 'Open'},
{'Title': 'problem 2', 'Description': 'awearfas', 'AssignedTo': 'person 2','Createdby':'Rohit16', 'Status': 'Closed'}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',user_details=user_details)
@app.route("/issue")
def issue():
	return render_template('issue.html',issue_details=issue_details)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in as {} !'.format(form.email.data), 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)

