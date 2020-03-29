
from Database import db

from flask import Flask,request,abort
app=Flask(__name__)

db.create_all();

if __name__=='__main__':
     app.run(debug=True)