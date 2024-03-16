from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.project.settings import Settings

db = SQLAlchemy()

def create_app(config_class=Settings):
    pass