#Importing all the required libraries
#1 mark(TASK 4.3) - all Flask related statement are present (import statements, creation of flask object, starting the server)
import flask
from flask import render_template, request
import sqlite3

app = flask.Flask(__name__) #create a Flask object 


@app.route('/')  #decorator #1 mark(TASK 4.3) - correct implementation of index method
def index():
    return render_template('index.html') #displaying index.html

@app.route('/votecount')  #decorator #1 mark(TASK 4.4) - correct implementation of vote_count method and connection to db to extract records
def vote_count():
    #connecting to given sqlite database and extracting relevant records
    connection = sqlite3.connect("election.db")
    cursor = connection.execute("SELECT Name, Class, COUNT(VID) FROM Vote INNER JOIN Candidate ON Vote.CID = Candidate.CID Group By Vote.CID Order By COUNT(VID) DESC") #2 marks(TASK 4.4) - 2 marks for correct inner join, correct group by & for putting output in descending order of total number of votes. 1 mark if have minor errors
    records = cursor.fetchall()
    connection.close()

    return render_template('votecount.html', html_records = records) #displaying votecount.html [Note: html_records is the Jinja variable in votecount.html] - 1 mark(TASK 4.4) - render correct html template with sending records to html file (give the mark if either Votecount or Votebreakdown html file has this)

@app.route('/votebreakdown', methods=['GET','POST']) #decorator #1 mark(TASK 4.5) - correct implementation of vote_breakdown method with different processing for GET and POST methods
def vote_breakdown():

	if request.method == "GET": #check if request is GET method (web app accessed by typing url in browser)

		return render_template('votebreakdown.html') #displaying votebreakdown.html with no other parameters
		
	else: #request is POST method (web app accessed by submitting html form with POST method)
                
		if 'candidate' in request.form: #checking if any html form input with the name 'userid'
			candidate_selected = request.form['candidate'] #1 mark(TASK 4.5) - extracting what user keyed in for the html form input 'candidate'

			#connecting to given sqlite database and extracting relevant records
			connection = sqlite3.connect("election.db")
			
			if candidate_selected == "all": 
				 #1 mark(TASK 4.5) - correct SQL when all is selected
				cursor = connection.execute("SELECT Voter.Name As Voter, Voter.Class, Candidate.Name AS Voted_For FROM Voter INNER JOIN Vote On Voter.VID = Vote.VID INNER JOIN Candidate ON Candidate.CID = Vote.CID") 
			else:
				#1 mark(TASK 4.5) - correct SQL when a specific candidate is selected
				cursor = connection.execute("SELECT Voter.Name As Voter, Voter.Class, Candidate.Name AS Voted_For FROM Voter INNER JOIN Vote On Voter.VID = Vote.VID INNER JOIN Candidate ON Candidate.CID = Vote.CID WHERE Candidate.Name = ?", (candidate_selected,))
			
			records = cursor.fetchall()
			connection.close()

			return render_template('votebreakdown.html', html_records = records) #displaying votebreakdown.html with other parameters [Note: html_records is the Jinja variable in votebreakdown.html]

	
if __name__ == "__main__":
    app.run() #calling the Flask object’s run() method to start the server