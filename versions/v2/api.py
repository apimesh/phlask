# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


v2_api = Blueprint('v2_api', __name__)

@v2_api.route('/v2')
def index():
    return jsonify(['Hello, Phlask!'])

@v2_api.route('/v2/version')
def version():
    return jsonify({
    		'name': "Phlask",
    		'version': "2"
    	})