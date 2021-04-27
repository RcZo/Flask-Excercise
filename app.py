from flask import Flask

from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')


# imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app, errors=errors)


initialize_db(app)
initialize_routes(api)
