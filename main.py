from flask import Flask
from router.router import Router
from router.routes import blueprint
from server.server import Server

flask = Flask(__name__)
router = Router(flask, blueprint)
server = Server(flask, router, 3333)

server.init()