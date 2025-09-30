from flask import Flask
from abstracts.abstracts import IDatabase, IRouter
from hypercorn.config import Config
from hypercorn.asyncio import serve

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
	
	async def _setup(self) -> None:
		self._router.setup_routes()
		await self._database.setup_database()

	async def _listen(self):
		config = Config()
		config.bind = [f"0.0.0.0:{self._PORT}"]

		try:
			await serve(self._flask, config)
		except Exception as error:
			print(f"Hey {error}")

	async def init(self):
		await self._setup()
		await self._listen()