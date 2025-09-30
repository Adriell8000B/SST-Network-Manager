from abstracts.abstracts import IDatabase
from prisma import Prisma

class Database(IDatabase):
	def __init__(self, prisma: Prisma) -> None:
		self._prisma = prisma

	async def _connect(self) -> None:
		error = await self._prisma.connect()

		if error != None:
			print(f"There was an error while connecting to mongodb: {error}")

	async def setup_database(self) -> None:
		await self._connect()