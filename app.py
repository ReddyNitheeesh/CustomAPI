
from flask import Flask,request,abort
app=Flask(__name__)

from Users import routes
from Posts import routesposts
from Database import db

db.create_all();

routes.init_routes(app)
routesposts.init_routes(app)

