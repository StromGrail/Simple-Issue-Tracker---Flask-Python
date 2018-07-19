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
    post = Post.query.all()
    userdetails
    for u in user :
        if u.email == userdetails:
            userdetails=u
    return render_template('home.html', user=user,userdetails=userdetails,post=post)



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
            if u.email == userdetails.email:
                username=u.username

        for u in user:
            if checkname == u.username and username != u.username:
                flag=True

        if flag==True:
            print('debug 1',form.Status.data)
            post = Post(title = form.Title.data, Description = form.Description.data, 
                AssignedTo = form.AssignedTo.data , Createdby = userdetails.username, Status = form.Status.data)
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


@app.route("/post/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title,post=post,userdetails=userdetails)

@app.route("/post/<int:post_id>/update",methods=['GET' ,'Post'])
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    #print(post.title,post.Description,post_id,post.id)
    form=PostIssueForm()
    if form.validate_on_submit():
        post.title=form.Title.data
        post.Description=form.Description.data
        post.Createdby=form.Createdby.data
        post.AssignedTo = form.AssignedTo.data
        db.session.commit()
        flash('Post updated! ', 'success')
        return redirect(url_for('post',post_id=post_id))
    elif request.method == 'GET':
        form.Title.data = post.title
        form.Description.data = post.Description
        form.Createdby.data = post.Createdby
        form.AssignedTo.data = post.AssignedTo
        return render_template('issue.html',title=post.title,post=post,userdetails=userdetails,form=form)

@app.route("/post/<int:post_id>/delete", methods=['GET','POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))