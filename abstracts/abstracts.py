from abc import ABC, abstractmethod
from typing import Any

from flask import Response
import prisma

class IRouter(ABC):
	@abstractmethod
	def setup_routes(self):
		pass

class IDatabase(ABC):
	@abstractmethod
	async def __connect(self) -> None:
		pass

	async def setup_database(self) -> None:
		pass

class IUserRepository(ABC):
	@abstractmethod
	async def retrieve_users(self) -> list[dict[str, Any]]:
		pass

	@abstractmethod
	async def create_user(
		self, _user_name: str,
		_user_password: str) -> prisma.models.users:
		pass

class IUserController(ABC):
	@abstractmethod
	async def get_users(self) -> Response:
		pass