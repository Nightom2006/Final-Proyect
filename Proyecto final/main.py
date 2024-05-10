#Import
from flask import Flask, render_template,request, redirect
#Connecting the database library

app = Flask(__name__)
#Connecting SQLite


#Running the page with the content
@app.route('/')
def index():
    #Outputting the objects from the DB
    #Assignment #2. Make it so that the DB objects are shown in index.html

    return render_template('index.html')

@app.route('/Datos')
def Datos():
    #Outputting the objects from the DB
    #Assignment #2. Make it so that the DB objects are shown in index.html

    return render_template('Datos.html')

if __name__ == "__main__":
    app.run(debug=True)