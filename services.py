# Flask Blueprint setup #

# Blueprint setup #
from flask import Blueprint
services = Blueprint('services', __name__)

# Route to various micro-services #
from py_bmi import bmi