from typing import Any, Union
from flask import Response, jsonify, request

from abstracts.abstracts import IUserController, IUserRepository

class UserController(IUserController):
	def __init__(self, user_repository: IUserRepository) -> None:
		self.__user_repository = user_repository

	async def get_users(self) -> Response:
		promise: list[dict[str, Any]] = []

		try:
			temp = await self.__user_repository.retrieve_users()

			if type(temp) == list[dict[str, Any]]:
				promise = temp

		except Exception as error:
			return jsonify(error.__class__.__name__)

		return jsonify(promise)

	async def add_user(self) -> Response:
		try:
			user_name = request.form["username"]
			user_password = request.form["password"]

			await self.__user_repository.create_user(user_name, user_password)
			return jsonify("User created!")

		except Exception as error:
			return jsonify(error.__class__.__name__)
