import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setup 
engine = create_engine('postgresql://user:password@localhost/servername')


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Vegetation = Base.classes.vegetation_actualnameoftableindatabase
Map2 = Base.classes.david_actualnameoftableindatabase
Map3 = Base.classes.dallas_actualnameoftableindatabase

# Flask Setup
app = Flask(__name__)


#### Flask Routes ####

# Landing Page route 
@app.route("/")
def index():
    return render_template("index.html")

# David route 
@app.route("/")
def david():
    return render_template("david.html")


# Dallas route 
@app.route("/")
def dallas():
    return render_template("dallas.html")

# Kerrie route 
@app.route("/")
def veggie():
    return render_template("veggie.html")

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all land types"""
    # Query all land types
    results = session.query(vegetation.evt_lf).all()

    session.close()

    # Convert list of tuples into normal list
    vegetation = list(np.ravel(results))

    return jsonify(vegetation)
