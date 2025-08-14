from flask import Flask
from flask import render_template, request, redirect
import json


app = Flask(__name__)

@app.route("/")
def site():
    pass