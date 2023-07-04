# Codebase on Python and Flask framework #
from flask import Flask
from services import *

app = Flask(__name__)
app.register_blueprint(services)

if __name__ == "__main__":
    app.run(debug=True)