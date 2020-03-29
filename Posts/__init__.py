from flask import Flask,request
from .routes import init_routes

app=Flask(__name__)

init_routes(app)

