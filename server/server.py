from flask import Flask

from abstracts.abstracts import ICors, IDatabase, IRouter

class Server:
	def __init__(
		self,
		flask: Flask,
		cors: ICors,
		router: IRouter,
		database: IDatabase,
		PORT: int
) -> None:
		self.__flask = flask
		self.__cors = cors
		self.__router = router
		self.__database = database
		self.__PORT = PORT
	
	async def __setup(self) -> None:
		self.__cors.setup_cors()
		self.__router.setup_routes()
		await self.__database.setup_database()

	def __listen(self):
		self.__flask.run(None, self.__PORT, debug=True)

	async def init(self):
		await self.__setup()
		self.__listen()