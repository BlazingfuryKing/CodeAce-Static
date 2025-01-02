from flask import Flask, render_template, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

db_filename = "cu_booking.db"

def connect_db(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        return conn
    except Error as e:
        print (e)

def avail(conn,date):
    sql = '''
        SELECT cubicle_no FROM cubicle
        WHERE cubicle_no NOT IN
        (SELECT cubicle.cubicle_no
            FROM cubicle 
        LEFT JOIN booking
            ON cubicle.cubicle_no = booking.cubicle_no
        WHERE date = ? OR maintenance = 1)
    '''
    cur = conn.execute(sql,(date,))
    avail_list = [i[0] for i in cur.fetchall()]
    return avail_list

def all_cubicle(conn):
    sql = '''
        SELECT cubicle.cubicle_no
            FROM cubicle 
    '''
    cur = conn.execute(sql)
    all_cubicle = [i[0] for i in cur.fetchall()]
    return all_cubicle

@app.route('/available/<date>/')
def available(date):
    conn = connect_db(db_filename)
    cubicles = all_cubicle(conn)
    available = avail(conn,date)
    conn.close()
    return render_template("available.html", date=date,
                           available=available, cubicles=cubicles)
    

if __name__ == '__main__':
    app.run(debug=True)
