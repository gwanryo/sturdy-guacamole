from flask import Flask
from os.path import join, dirname
from dotenv import load_dotenv
from database import Database

import logging
import sys
import os

# Logging
logging.basicConfig(
    format = '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt = '%Y/%m/%d %p %I:%M:%S',
    level = logging.INFO,
    handlers = [
        # logging.FileHandler("runtime.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

conn = {
    'DB_HOST': os.environ.get('DB_HOST'),
    'DB_PORT': os.environ.get('DB_PORT'),
    'DB_NAME': os.environ.get('DB_NAME'),
    'DB_USER': os.environ.get('DB_USER'),
    'DB_PASS': os.environ.get('DB_PASS'),
    'DB_CONN_MIN': os.environ.get('DB_CONN_MIN'),
    'DB_CONN_MAX': os.environ.get('DB_CONN_MAX')
}

db = Database(conn)

def create_app():
    app = Flask(__name__)

    from route import stats, concept, table
    app.register_blueprint(stats.stats, url_prefix='/stats')
    app.register_blueprint(concept.concept, url_prefix='/concept')
    app.register_blueprint(table.table, url_prefix='/table')

    @app.route("/", methods = ['GET'])
    def root():
        return "<img src='https://salt-pro.com/wp-content/uploads/2017/01/may_the_force_be_with_you___yoda_flag_by_osflag-d9xe904.jpg'/>"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
