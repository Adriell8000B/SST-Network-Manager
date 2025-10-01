from typing import Any
from flask import Response, jsonify

from abstracts.abstracts import IUserController, IUserRepository

class UserController(IUserController):
	def __init__(self, user_repository: IUserRepository) -> None:
		self._user_repository = user_repository

	async def get_users(self) -> Response:
		promise: list[dict[str, Any]] = []

		try:
			promise = await self._user_repository.retrieve_users()
		except Exception as error:
			print(f"Coudln't JSONIFY users due to an error: {error}")

		return jsonify(promise)