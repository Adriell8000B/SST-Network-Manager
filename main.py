from flask import Flask
from prisma import Prisma
from database.database import Database
from router.router import Router
from router.routes import blueprint
from server.server import Server
from utils.utils import get_env_string, setup_environment

setup_environment()

flask = Flask(__name__)
prisma = Prisma()

router = Router(flask, blueprint)
database = Database(prisma)
server = Server(
	flask,
	router,
	database,
	int(get_env_string("PORT"))
)

server.init()