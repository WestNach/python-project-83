import os
from flask import \
    Flask, \
    render_template, \
    request, flash, \
    url_for, redirect, \
    get_flashed_messages


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')