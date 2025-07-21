from flask import Flask
from src.main.routes.calculators import calc_rout_bp

app = Flask(__name__)

app.register_blueprint(calc_rout_bp)