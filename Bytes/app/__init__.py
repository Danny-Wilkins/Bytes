from flask import Flask

app = Flask(__name__, static_url_path = "", static_folder = "/templates/Static")
from app import views
