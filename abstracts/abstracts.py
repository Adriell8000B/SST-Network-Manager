from abc import ABC, abstractmethod
from typing import Any, Union

from flask import Response
import prisma

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
	async def retrieve_users(self) -> Union[list[dict[str, Any]], str]:
		pass

	@abstractmethod
	async def create_user(
		self,
		_user_name: str,
		_user_password: str
	)-> Union[prisma.models.users, str]:
		pass

	@abstractmethod
	async def remove_user(self, user_id: str) -> Union[None, str]:
		pass

class IUserController(ABC):
	@abstractmethod
	async def get_users(self) -> Response:
		pass

	@abstractmethod
	async def add_user(self) -> Response:
		pass

class ICors(ABC):
	@abstractmethod
	def setup_cors(self) -> None:
		pass