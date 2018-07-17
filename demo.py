from flask import Flask , render_template
app = Flask(__name__)
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


if __name__ == '__main__':
	app.run(debug=True)