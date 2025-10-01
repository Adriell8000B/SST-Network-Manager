from flask import Flask

from abstracts.abstracts import IRouter, IUserController
from router.routes import create_view_functions

class Router(IRouter):
	def __init__(self, flask: Flask, user_controller: IUserController) -> None:
		self._flask = flask
		self._user_controller = user_controller
		self._views = create_view_functions(self._user_controller)

	def setup_routes(self):
		self._flask.route("/")(self._views["index"])
		self._flask.route("/foo")(self._views["foo"])
