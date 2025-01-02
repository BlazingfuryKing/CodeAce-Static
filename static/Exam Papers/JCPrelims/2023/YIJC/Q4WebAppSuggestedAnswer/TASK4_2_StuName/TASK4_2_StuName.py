from flask import *

app = Flask(__name__)                               


@app.route('/')                           
def index():                              
    return render_template('index.html')  #1m render index.html in default route

         

app.run(debug = False, port = 5000)   
   


