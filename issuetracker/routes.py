from flask import render_template, url_for, flash, redirect
from issuetracker import app, db
from issuetracker.forms import RegistrationForm, LoginForm
from issuetracker.models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    user = User.query.all()
    return render_template('home.html', user=user)


@app.route("/issue")
def about():
    return render_template('issue.html', title='issue')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        user= User(FirstName=form.FirstName.data,LastName= form.LastName.data,username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.all()
        for u in user :
            #for debugging purpose only
            print(u.email,u.password)
            if form.email.data == u.email:
                if form.password.data == u.password:
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)