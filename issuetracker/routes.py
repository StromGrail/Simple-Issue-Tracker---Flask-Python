from flask import render_template, url_for, flash, redirect,request
from issuetracker import app, db
from issuetracker.forms import RegistrationForm, LoginForm, PostIssueForm
from issuetracker.models import User, Post

userdetails = ''


@app.route("/")
@app.route("/home")
def home():
    user = User.query.all()
    userinfo=None
    for u in user :
        if u.email == userdetails:
            userinfo=u
    return render_template('home.html', user=user,userinfo=userinfo)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        global userdetails
        userdetails = form.username.data
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
            if form.email.data == u.email:
                if form.password.data == u.password:
                    global userdetails
                    userdetails = form.email.data
                    print(userdetails)
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/issue", methods=['GET', 'POST'])
def postissue():
    form = PostIssueForm(request.form)
    if request.method == "POST" :
        global userdetails
        user = User.query.all()
        flag,username ,checkname = False,'',form.AssignedTo.data 
        print(checkname)
        for u in user:
            if u.email== userdetails:
                username=u.username

        for u in user:
            if checkname == u.username and username != u.username:
                flag=True

        if flag==True:
            print('debug 1')
            post = Post(title = form.Title.data, Description = form.Description.data, 
                AssignedTo = form.AssignedTo.data , Createdby = username, Status = form.Status.data)
            db.session.add(post)
            db.session.commit()
            flash('You post has been created !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Something went wrong .... Please try again.', 'danger')   
            if flag==False:
                flash('Wrong Assignment', 'danger')   
                     

    return render_template('issue.html',title= 'New Issue', username=userdetails , form= form)