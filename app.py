from flask import Flask, render_template, redirect, jsonify, request
import pandas as pd
import datetime as dt
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)


########Home Page###########

@app.route("/")
def welcome():
    return render_template('index.html')
    #return render_template('index.html', data=big_list)


########Circle Pack###########

@app.route("/circlepack")
def circlepack():
    return render_template('/circlepack.html')


########Bar Graph###########

@app.route("/bar")
def bar():
    return render_template('/bar.html')

if __name__ == "__main__":
    app.run()