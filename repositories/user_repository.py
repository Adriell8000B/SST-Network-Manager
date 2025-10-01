from typing import Any, List

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