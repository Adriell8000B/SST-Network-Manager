from pymongo import AsyncMongoClient
from abstracts.abstracts import IMongoFactory

class MongoFactory(IMongoFactory):
	def __init__(self, uri: str) -> None:
		self._uri = uri
	
	def create_async_client(self) -> AsyncMongoClient:
		return AsyncMongoClient(self._uri)