#!/usr/bin/python3
""" Init file """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import (PEP8 will complain, but it's okay for this specific case)
from api.v1.views.index import *
