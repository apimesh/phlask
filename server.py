# -*- coding: utf-8 -*-
from flask import Flask


def create_server():
    app = Flask(__name__)

    from versions.default import default_api
    app.register_blueprint(default_api)

    from versions.v1.api import v1_api
    app.register_blueprint(v1_api)

    from versions.v2.api import v2_api
    app.register_blueprint(v2_api)
    
    return app
