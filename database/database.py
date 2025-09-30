from abstracts.abstracts import IDatabase
from prisma import Prisma

class Database(IDatabase):
	def __init__(self, prisma: Prisma) -> None:
		self._prisma = prisma

	def _connect(self) -> None:
		error = self._prisma.connect()

		if error != None:
			print(f"There was an error while connecting to mongodb: {error}")

	def setup_database(self) -> None:
		self._connect()