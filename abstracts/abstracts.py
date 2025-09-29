from pymongo import AsyncMongoClient
from abc import ABC, abstractmethod

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass

class IMongoFactory(ABC):
	@abstractmethod
	@staticmethod
	def create_async_client(uri: str) -> AsyncMongoClient:
		pass

class IDatabase(ABC):
	@abstractmethod
	def _connect(self) -> None:
		pass

	def setup_database(self) -> None:
		pass