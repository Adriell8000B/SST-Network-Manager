from flask import Flask
from asyncio import run
from prisma import Prisma
from controllers.user_controller import UserController
from database.database import Database
from router.router import Router
from router.routes import blueprint
from server.server import Server
from utils.utils import get_env_string, setup_environment
from repositories.user_repository import UserRepository

setup_environment()

flask = Flask(__name__)
prisma = Prisma()

user_repository = UserRepository(prisma)
user_controller = UserController(user_repository)
router = Router(flask, blueprint)
database = Database(prisma)

server = Server(
	flask,
	router,
	database,
	int(get_env_string("PORT"))
)

if __name__ == "__main__":
	run(server.init())