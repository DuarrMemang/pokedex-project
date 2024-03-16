from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from apps import app
from apps.model import *
from apps.forms import *

@app.route('/')
def index():
    return render_template('index.html')