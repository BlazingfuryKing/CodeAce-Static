from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("rentalsdue.html")


@app.route("/display",methods = ["POST"])
def display():
    data = request.form
    edate = data["date"]
    conn = sqlite3.connect("JPFashion.db")
    query = """select pr.ID,p.CatalogueNumber,c.Email,c.ContactNumber
    from Product as p,CustomerRental as cr,ProductRental as pr,Customer as c
    where cr.EndDate = ? and
        pr.Returned = 0 and
        cr.ID = pr.ID and
        pr.CatalogueNumber = p.CatalogueNumber and
        cr.Email = c.Email"""
    result = conn.execute(query,(edate,))
    result = result.fetchall()
    conn.close()
    return render_template("TASK4_4_21S22_TAN_SOONPING.html",result=result)



if __name__ == "__main__":
    app.run(port = 5678,debug = True)

