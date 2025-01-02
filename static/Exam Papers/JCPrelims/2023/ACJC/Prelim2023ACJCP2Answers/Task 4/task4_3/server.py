from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) #to initialize the flask app

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/display')
def display():
    comp_id = request.args['comp_id']
    mem_id = request.args['mem_id']
    score = request.args['score']
    conn = sqlite3.connect('club.db')
    conn.execute("INSERT INTO Scores VALUES (?,?,?)", (comp_id, mem_id, score))
    conn.commit()
    conn.close()
    return "success!"

app.run()



