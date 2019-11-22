from flask import Flask
from . import compare

def init_service():
    app = Flask(__name__)
    app.register_blueprint(compare.bp, url_prefix="/compare")
    return app
    