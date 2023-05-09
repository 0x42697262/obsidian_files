import os
from flask import Flask, render_template, jsonify, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY="dev",
            DATABASE=os.path.join(app.instance_path, 'mp2.sqlite'),
            )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')


    from . import functions

    @app.route('/submitprocess', methods=['POST'])
    def submit_input():
        functions.insert_to_db(request.json['process'], request.json['quantum'])

        return jsonify("sdf")


    return app
