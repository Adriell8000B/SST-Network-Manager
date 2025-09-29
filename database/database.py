from abstracts.abstracts import IDatabase
from factories.mongo_factory import MongoFactory

class Database(IDatabase):
	def __init__(self, uri: str) -> None:
		self._uri = uri
		self._mongo_client = MongoFactory.create_async_client(self._uri)
	
	def _connect(self) -> None:
		try:
			self._mongo_client.get_default_database()
		except Exception as error:
			print(f"Coudln't connect to MongoDB due to an error: {error}")
	
	def setup_database(self) -> None:
		self._connect()