from abc import ABC, abstractmethod

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass