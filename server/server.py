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
	
	async def __setup(self) -> None:
		self._router.setup_routes()
		await self._database.setup_database()
	
	def __listen(self):
		self._flask.run(None, self._PORT, debug=True)

	async def init(self):
		await self.__setup()
		self.__listen()