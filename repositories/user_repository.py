from typing import List
from prisma.models import users
from abstracts.abstracts import IUserRepository
from prisma import Prisma

class UserRepository(IUserRepository):
	def __init__(self, prisma: Prisma) -> None:
		self._prisma = prisma

	async def retrieve_users(self) -> List[users]:
		response = await self._prisma.users.find_many()

		if response != List[users]:
			print(f"Couldn't get users")

		return response