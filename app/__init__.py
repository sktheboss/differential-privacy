""" Application Initializer """
import time
import logging
from http import HTTPStatus
from flask import Flask, g, request, render_template, flash, session
from app.config.db import DatabaseServer
from app.common.response import Response
from app.config.config import FLASK_ENV, ProductionConfig, config_by_name

# Database initialization
db = DatabaseServer.get_instance()

# Create application
app = Flask(__name__)
app.config.from_object(config_by_name.get(FLASK_ENV, ProductionConfig))

# Logging Configuration``
logging.basicConfig(filename='logs/smart_noise_module.log', 
                    filemode='a',
                    level=logging.DEBUG,
                    format="[%(asctime)s][%(levelname)s]:- %(message)s",
                    datefmt='%d-%b-%y %H:%M:%S')

# register blueprint with app

# Initialize database with flask app
# db.init_app(app)

@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    # flash("hello", "info")
    # flash("hello", "danger")
    # flash("hello", "warning")
    # flash("hello", "success")

    return render_template('/index.html')

@app.route("/query", methods=['GET'])
def query():
    return render_template('/base.html')