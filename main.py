from asyncio import run

from flask import Flask
from flask_cors import CORS
from prisma import Prisma

from controllers.user_controller import UserController
from database.database import Database
from middlewares.cors import Cors
from repositories.user_repository import UserRepository
from router.router import Router
from server.server import Server
from utils.utils import get_env_string, setup_environment

setup_environment()

flask = Flask(__name__)
cors = CORS()
prisma = Prisma()

cors_middleware = Cors(cors, flask)

user_repository = UserRepository(prisma)
user_controller = UserController(user_repository)
router = Router(flask, user_controller)
database = Database(prisma)

server = Server(
	flask,
	cors_middleware,
	router,
	database,
	int(get_env_string("PORT"))
)

# Production environment

server.setup_wsgi()

try:
	run(database.setup_database())
except Exception as error:
	print(f"Couldn't connect due to an error: {error}")
	raise

# Development environment

if __name__ == "__main__":
	run(server.init())