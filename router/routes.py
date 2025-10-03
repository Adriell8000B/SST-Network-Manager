from flask import render_template

from abstracts.abstracts import IUserController

def create_view_functions(controller: IUserController):
	async def users_view():
		return await controller.get_users()

	def login_view():
		return render_template("login.html")
	
	return {
		"users": users_view,
		"login": login_view
	}