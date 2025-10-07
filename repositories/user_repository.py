from typing import Any, List, Optional, Union

from prisma import Prisma
from prisma.models import users

from abstracts.abstracts import IUserRepository

class UserRepository(IUserRepository):
	def __init__(self, prisma: Prisma) -> None:
		self._prisma = prisma

	async def retrieve_users(self) -> list[dict[str, Any]]:
		response = await self._prisma.users.find_many()

		if response != List[users]:
			print(f"Couldn't retrieve users")

		return [user.model_dump() for user in response]

	async def create_user(self, _user_name: str, _user_password: str) -> Union[users, str]:
		try:
			new_user = await self._prisma.users.create(
				data={
					"user_name": _user_name,
					"user_password": _user_password
				}
			)
			return new_user

		except Exception as error:
			return error.__class__.__name__