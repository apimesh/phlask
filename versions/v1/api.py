# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


v1_api = Blueprint('v1_api', __name__)

@v1_api.route('/v1')
def index():
    return jsonify(['Hello, Phlask!'])

@v1_api.route('/v1/version')
def version():
    return jsonify({
    		'name': "Phlask",
    		'version': "1"
    	})