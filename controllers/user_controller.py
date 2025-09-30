from typing import Any, Coroutine, List
from prisma.models import users
from abstracts.abstracts import IUserController, IUserRepository

class UserController(IUserController):
	def __init__(self, user_repository: IUserRepository) -> None:
		self._user_repository = user_repository
	
	def get_users(self) -> Coroutine[Any, Any, List[users]]:
		return self._user_repository.retrieve_users()