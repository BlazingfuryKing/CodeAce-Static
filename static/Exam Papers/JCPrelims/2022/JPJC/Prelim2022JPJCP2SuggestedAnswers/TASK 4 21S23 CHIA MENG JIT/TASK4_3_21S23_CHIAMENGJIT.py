import sqlite3, flask
from flask import render_template, request, url_for

app = flask.Flask(__name__)

@app.route('/')
def home(): #have a form only with the email address input
    return render_template("index.html")

#if users entered an email address that already exists in the form, prompts the error message
@app.route('/error/')
def error():
    return "<h1>Email already exists in database! Click <a href = '/' > here </a> to return</h1>"
    #provides a link to click to return back to home

@app.route('/<email>/')
def check(email):
    #check if email in database
    db = sqlite3.connect("JPFashion.db")
    cur = db.execute("SELECT email FROM Customer WHERE email = ?", (email,))
    for item in cur:
        if item == email:
            #if the email already exists in the database, will redirect to /error/ page
            db.close()
            return url_for('/error/')
    db.close()
    return render_template("create.html") #this html form will route to create()

@app.route('/<email>/status/', methods = ['POST'])
def create(email):
    #retrieval of all attributes from the database, with email passed as the input
    db = sqlite3.connect("JPFashion.db")
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        contact = request.form["contact"]
        dob = request.form["dob"]
        address = request.form["address"]
    db.execute('''
            INSERT INTO Customer(Email, FirstName, LastName, ContactNumber, DOB, Address)
            VALUES(?,?,?,?,?,?)
            ''', (email, firstname, lastname, contact, dob, address)
               )
    db.close()
    return "New account created successfully"

@app.route('/rental/dued/')
def rental_dued():
    #load for task 4.4
    return render_template('rentalsdue.html')

@app.route('/rental/dued/display/', methods = ['GET'])
def rental_output():
    if request.method == 'GET':
        enddate = request.args['enddate']

    #query for required output
    db = sqlite3.connect("JPFashion.db")
    cur = db.execute('''
                    SELECT CustomerRental.ID, ProductRental.CatalogueNumber, Customer.Email, Customer.ContactNumber
                    FROM CustomerRental, ProductRental, Customer
                    WHERE CustomerRental.EndDate = ? AND ProductRental.ID = CustomerRental.ID AND CustomerRental.Email = Customer.Email
                    '''
                     , (enddate, )
                     )
    results_lst = []
    for record in cur:
        results_lst.append(record)
    db.close()
    return render_template("rental_output_results.html", results_lst = results_lst)
    
if __name__ == "__main__":
    app.run(port = 5678, debug = True)
    
