from abc import ABC, abstractmethod
from typing import Any

from flask import Response

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
	async def retrieve_users(self) -> list[dict[str, Any]]:
		pass

class IUserController(ABC):
	@abstractmethod
	async def get_users(self) -> Response:
		pass