import os
from flask import Flask

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
        return "index() page"

    @app.route('/test')
    def test():
        db.insert_process(1);
        db.insert_job(1, 1, 0, 10)
        print('dddd')
        db.commit()

        return "OK!"
    
    @app.route('/commit')
    def commit():

        return "commited!"

    return app
