from flask import Flask
from database.database import Database
from router.router import Router
from router.routes import blueprint
from server.server import Server

flask = Flask(__name__)
router = Router(flask, blueprint)
database = Database("")
server = Server(flask, router, database,3333)

server.init()