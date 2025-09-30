from abc import ABC, abstractmethod
from typing import List

from prisma.models import users

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

class IUserRepository(ABC):
	@abstractmethod
	async def get_users(self) -> List[users]:
		pass