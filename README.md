# Simple Issue Tracker
> Created a web application using Python,Python- Flask,Flask SQLAlchemy,Flask_bcrypt,Flaskwtf and FlaskWtforms.


## Intro

> This application provides a stage for user to perform CRUD operations i.e. create, read, update and delete for the issues after creating or login a secured hashed password account.


## Operating system
```
Ubuntu
```



# How to run

```
1. open terminal and direct it to the locations where the Simple-Issue-Tracker---Flas-Python is located. 

2. Run the below command.
      a. pip3 install -r requirements.txt 
      b. python run.py
      c. go to http://127.0.0.1:5000/ 
      
3. To create new database for the user
    a. follow the first step
    b. type 'python' in terminal
      b1. from issuetracker import db
      b2. from issuetracker.models import User, Post
      b3. User.query.delete()
      b4. Post.query.delete()
      b5. db.session.commit()
      b6. exit()

4. To close the debug feature
   a. open run.py
   b. make 'debug=True' to 'debug=False' in app.run
  
```


# Working demonstration
> https://www.youtube.com/watch?v=JU8cDpZsSj4


# Refrence 
1. > http://flask.pocoo.org/docs/1.0/tutorial/
2. > https://www.tutorialspoint.com/flask
3. > https://hackr.io/tutorials/learn-flask
4. > https://www.fullstackpython.com/flask.html
5. > http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
6. > https://www.youtube.com/watch?v=ZVGwqnjOKjk

# Website
   > https://stromgrail.github.io/
