from flask import Flask
from abstracts.abstracts import IDatabase, IRouter

class Server:
	def __init__(
		self,
		flask: Flask, 
		router: IRouter,
		database: IDatabase,
		PORT: int
) -> None:
		self._flask = flask
		self._router = router
		self._database = database
		self._PORT = PORT
	
	def _setup(self) -> None:
		self._router.setup_routes()
		self._database.setup_database()
	
	def _listen(self):
		try:
			self._flask.run(None, self._PORT)
		except Exception as error:
			print(f"Coudln't start the server due to an error: {error}")

	def init(self):
		self._setup()
		self._listen()
