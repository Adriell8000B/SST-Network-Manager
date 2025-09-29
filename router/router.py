from flask import Blueprint, Flask

from abstracts.abstracts import IRouter

class Router(IRouter):
	def __init__(self, flask: Flask, blueprint: Blueprint) -> None:
		self._flask = flask
		self._blueprint = blueprint
	
	def setup_routes(self):
		self._flask.register_blueprint(self._blueprint)
