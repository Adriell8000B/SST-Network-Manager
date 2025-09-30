from abc import ABC, abstractmethod
from typing import Any, Coroutine, List

from prisma.models import users

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass

class IDatabase(ABC):
	@abstractmethod
	async def _connect(self) -> None:
		pass

	async def setup_database(self) -> None:
		pass

class IUserRepository(ABC):
	@abstractmethod
	async def retrieve_users(self) -> List[users]:
		pass

class IUserController(ABC):
	@abstractmethod
	def get_users(self) -> Coroutine[Any, Any, List[users]]:
		pass