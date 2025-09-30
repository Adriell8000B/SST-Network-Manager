from abc import ABC, abstractmethod

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass

class IDatabase(ABC):
	@abstractmethod
	def _connect(self) -> None:
		pass

	def setup_database(self) -> None:
		pass