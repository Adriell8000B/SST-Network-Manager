from pymongo import AsyncMongoClient
from abc import ABC, abstractmethod

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass

class IMongoFactory(ABC):
	@abstractmethod
	def create_async_client(self) -> AsyncMongoClient:
		pass