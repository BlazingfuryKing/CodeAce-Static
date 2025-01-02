import flask, sqlite3

app = flask.Flask(__name__)
db = sqlite3.connect("bank.db") #1m
db.row_factory = sqlite3.Row


@app.route('/') #1m
def index():
    results = []

    records = db.execute("SELECT * FROM Customer").fetchall() #1m
    ##sqlite.Row object is immutable
    ##need another field to identify as Priority or Customer
    for record in records: #1m
        priority = 'Priority' if record["isPriority"] == 1 else "Customer"
        results.append( (record,priority))
    return flask.render_template('index.html', results = results,) #1m

if __name__ == '__main__':
    app.run(debug=False)
## html 1m content, 1m structure, 1m format