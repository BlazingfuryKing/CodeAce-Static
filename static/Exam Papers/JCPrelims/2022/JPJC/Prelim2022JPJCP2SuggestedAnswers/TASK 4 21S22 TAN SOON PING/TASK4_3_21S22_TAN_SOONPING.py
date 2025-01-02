from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/second", methods = ["POST"])
def second_input():
    data = request.form
    email = data["email"]
    conn = sqlite3.connect("JPFashion.db")
    result = conn.execute("select * from Customer where Email = ?",(email,)).fetchone()
    conn.close()
    if result == None:
        return render_template("new_customer.html")
    else:
        return render_template("customer_exist.html",result=result)
    


@app.route("/display",methods = ["POST"])
def display():
    data = request.form
    conn = sqlite3.connect("JPFashion.db")
    email = data.get("re_email")
    if email == None:
        
        Email = data["email"]
        FirstName = data["fn"]
        LastName = data["ln"]
        ContactNumber = data["cn"]
        DOB = data["dob"]
        Address = data["address"]
        conn.execute("insert into Customer values (?,?,?,?,?,?)",(Email,FirstName,LastName,ContactNumber,DOB,Address))
        conn.commit()
    conn.close()
    return render_template("Display.html")

if __name__ == "__main__":
    app.run(port = 5678, debug = True)

