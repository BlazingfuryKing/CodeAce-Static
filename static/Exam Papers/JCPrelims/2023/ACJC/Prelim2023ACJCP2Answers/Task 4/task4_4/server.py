from flask import render_template, request, Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/results')
def results():
    comp_id = request.args['comp_id']
    conn = sqlite3.connect('club.db')
    data = conn.execute('''SELECT Members.Mem_ID, Mem_Name, Score FROM Members
                                INNER JOIN Scores ON Members.Mem_ID = Scores.Mem_ID
                                WHERE Comp_ID = ?
                                Order By Score DESC''', (comp_id,))
    
    return render_template('results.html', data = data)

app.run()


    
                              


