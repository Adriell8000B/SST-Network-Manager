from typing import Any, Union
from flask import Response, jsonify, request

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

	async def add_user(self) -> Union[None, str]:
		try:
			user_name = request.form["username"]
			user_password = request.form["password"]

			await self._user_repository.create_user(user_name, user_password)

			return None
		except Exception as error:
			return error.__class__.__name__
