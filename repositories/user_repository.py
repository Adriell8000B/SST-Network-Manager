from typing import Any, Union

from prisma import Prisma
from prisma.models import users

from abstracts.abstracts import IUserRepository

class UserRepository(IUserRepository):
	def __init__(self, prisma: Prisma) -> None:
		self.__prisma = prisma

	async def retrieve_users(self) -> Union[list[dict[str, Any]], str]:
		try:
			response = await self.__prisma.users.find_many()
			return [ user.model_dump() for user in response ]
		except Exception as error:
			return error.__class__.__name__

	async def create_user(
			self,
			_user_name: str,
			_user_password: str,
			_user_ip: str
		) -> Union[users, str]:
		try:
			new_user = await self.__prisma.users.create(
				data={
					"user_name": _user_name,
					"user_password": _user_password,
					"user_ip": _user_ip
				})

			return new_user

		except Exception as error:
			return error.__class__.__name__

	async def remove_user(self, user_id: str) -> Union[None, str]:
		try:
			await self.__prisma.users.delete(where={ "id": user_id })
			return

		except Exception as error:
			return error.__class__.__name__