from abstracts.abstracts import IAuthController

class AuthController(IAuthController):
	async def login(self) -> None:
		return await super().login()