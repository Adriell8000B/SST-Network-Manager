from flask import Flask
from database.database import Database
from router.router import Router
from router.routes import blueprint
from server.server import Server
from utils.utils import get_env_string, setup_environment

setup_environment()

flask = Flask(__name__)
router = Router(flask, blueprint)
database = Database(get_env_string("MONGODB_URI"))
server = Server(
	flask,
	router,
	database,
	int(get_env_string("PORT"))
)

server.init()