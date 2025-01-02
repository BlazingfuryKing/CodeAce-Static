from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('SUPERMARKET.db')

    data = conn.execute('''SELECT Customer.Name, Item.Name, Quantity
					FROM Item INNER JOIN
					(Customer INNER JOIN Purchase ON Customer.CustomerNumber = Purchase.CustomerNumber)
                    ON Item.ItemID = Purchase.ItemID
					WHERE DateTime >= 20240101 AND DateTime <= 20241231''')
    lst = data.fetchall()

    conn.close()

    return render_template('index.html', lst=lst)


app.run()
