from flask import Flask, render_template
from sqlite3 import *

app = Flask(__name__)


@app.route('/')
def index():
    db = connect('LIBRARY.db')
    c = db.cursor()

    c.execute('''SELECT FamilyName, GivenName, Title \
FROM Book, Member, Loan \
WHERE Returned = 'FALSE' \
AND Book.BOOKID = Loan.BookID \
AND Member.MemberNumber = Loan.MemberNumber;''')

    data = c.fetchall()

    db.close()

    return render_template('index.html', data=data)


app.run(debug=True, port=5001)
