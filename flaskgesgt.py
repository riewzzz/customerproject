from flask import Flask
import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="game"
)

app = Flask(__name__)

@app.route("/")
def home():
    myhtml = ""
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from customers")
    for i in mycursor:
        myhtml = myhtml + str(i)
    return myhtml


if __name__=='__main__':
    app.run()
