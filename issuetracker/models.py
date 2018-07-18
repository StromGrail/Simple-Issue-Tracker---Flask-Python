from datetime import datetime
from issuetracker import db
'''
Email,Username,FirstName,LastName, Password, AccessToken
'''

class User(db.Model):
    AccessToken = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',  lazy=True)

    def __repr__(self):
        return "User('{}', '{}',)".format(self.username,self.email)

'''Title, Description, AssignedTo (User relation), 
Createdby (User relation), Status (Open, Closed) '''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Description = db.Column(db.Text, nullable=False)
    AssignedTo = db.Column(db.Integer, nullable=False)
    Createdby= db.Column(db.Integer, db.ForeignKey('user.AccessToken'), nullable=False)
    Status = db.Column(db.Boolean,default=True)

    def __repr__(self):
    	return "Post('{}', '{}')".format(self.title,self.date_posted)