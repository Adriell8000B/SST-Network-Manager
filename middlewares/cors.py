from abstracts.abstracts import ICors
from flask_cors import CORS
from flask import Flask

from utils.utils import get_env_string

class Cors(ICors):
	def __init__(self, cors: CORS,flask: Flask) -> None:
		self.__cors = cors
		self.__flask = flask
	
	def setup_cors(self) -> None:
		self.__cors.init_app(self.__flask, resources={
			r"/api/*": {
				"origins": get_env_string("ALLOWED_ORIGIN"),
				"methods": ["GET", "POST"],
				"allow_headers": ["Content-Type", "Authorization"]
			}
		})