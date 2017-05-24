# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


default_api = Blueprint('default_api', __name__)

@default_api.route('/')
def index():
    return jsonify(['Hello, Phlask!'])
