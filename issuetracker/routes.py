from flask import render_template, url_for, flash, redirect,request
from issuetracker import app, db
from issuetracker.forms import RegistrationForm, LoginForm, PostIssueForm
from issuetracker.models import User, Post

userdetails = None


@app.route("/")
@app.route("/home")
def home():
    global userdetails
    user = User.query.all()
    userdetails
    for u in user :
        if u.email == userdetails:
            userdetails=u
    return render_template('home.html', user=user,userdetails=userdetails)



@app.route("/register", methods=['GET', 'POST'])
def register():
    global userdetails
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        userdetails = form.username.data
        user= User(FirstName=form.FirstName.data,LastName= form.LastName.data,username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form,userdetails=userdetails)


@app.route("/login", methods=['GET', 'POST'])
def login():
    global userdetails
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.all()
        for u in user :
            if form.email.data == u.email:
                if form.password.data == u.password:
                    userdetails = form.email.data
                    print(userdetails)
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form,userdetails=userdetails)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    global userdetails
    userdetails=None
    return redirect(url_for('home'))


@app.route("/issue", methods=['GET', 'POST'])
def postissue():
    global userdetails
    form = PostIssueForm(request.form)
    if request.method == "POST" and userdetails!=None:
        user = User.query.all()
        flag,username ,checkname = False,'',form.AssignedTo.data 
        print(checkname)
        for u in user:
            if u.email== userdetails.email:
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
    elif userdetails==None:
        flash('Login to proceed', 'danger')
        return redirect(url_for('login'))  

    return render_template('issue.html',title= 'New Issue', userdetails=userdetails , form= form)