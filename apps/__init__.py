from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_session import Session
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__, template_folder = "views")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

if not app.config["SQLALCHEMY_DATABASE_URI"]:
    raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set")


db = SQLAlchemy(app) 
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
cors = CORS(app)

from apps.users.routes import *
from apps.users.model import *