from flask import render_template

from abstracts.abstracts import IUserController

def create_view_functions(controller: IUserController):
	async def users_view():
		return await controller.get_users()
	
	async def add_user():
		return await controller.add_user()
	
	return {
		"users": users_view,
		"add-user": add_user
	}