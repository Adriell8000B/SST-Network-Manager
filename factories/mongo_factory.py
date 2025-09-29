from pymongo import AsyncMongoClient
from abstracts.abstracts import IMongoFactory

class MongoFactory(IMongoFactory):
	@staticmethod
	def create_async_client(uri: str) -> AsyncMongoClient:
		return AsyncMongoClient(uri)