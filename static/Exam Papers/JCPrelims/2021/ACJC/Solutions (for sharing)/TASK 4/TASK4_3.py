from flask import *
import sqlite3

app = Flask(__name__) # set up Flask and run

# set up a route to render the HTML form
# for a text box, three checkboxes and submit button in the HTML form
@app.route("/")
def root():
    return render_template("form.html")

# set up another route to render the display HTML document
@app.route("/result", methods=["POST"])
def result():
    # retrieve input from the HTML form
    location = request.form["location"]
    allergies = request.form.getlist("allergy")

    # connect to the SQL database (no need to check for close)
    connection = sqlite3.connect("bento_company.db")
    connection.row_factory = sqlite3.Row

    # SQL statement to extract data for the given location
    # use of AND to join tables (or other means)
    bentos = connection.execute('''
                                SELECT *
                                FROM Kiosk, KioskBento, BentoBox
                                WHERE Kiosk.KioskID = KioskBento.KioskID
                                AND KioskBento.BentoName = BentoBox.BentoName
                                AND Kiosk.Location = ?
                                ''', (location,)).fetchall()
    connection.close()
    
    result = []

    # filter out bentos based on allergies
    for i in bentos:
        if ("egg" in allergies and i['ContainEgg'] == 1 or
            "nut" in allergies and i['ContainNut'] == 1 or
            "seafood" in allergies and i['ContainSeafood'] == 1):
            continue

        result.append([i['BentoName'], i['SellPrice']])        

    # render the HTML document and pass result
    return render_template("result.html", result=result)

app.run()
