from prisma import Prisma

from abstracts.abstracts import IDatabase

class Database(IDatabase):
	def __init__(self, prisma: Prisma) -> None:
		self.__prisma = prisma

	async def __connect(self) -> None:
		if not self.__prisma.is_connected():
			try:
				await self.__prisma.connect()
			except Exception as e:
				print(f"Couldn't connect to db: {e}")

	async def setup_database(self) -> None:
		await self.__connect()