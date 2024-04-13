import os
from page_analyzer.config import Config
from flask import \
    Flask, \
    render_template, \
    request, flash, \
    url_for, redirect, \
    get_flashed_messages


app = Flask(__name__)
app.config.from_object(Config)