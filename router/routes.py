from flask import render_template

from abstracts.abstracts import IUserController

def create_view_functions(controller: IUserController):
	async def index_view():
		return await controller.get_users()
	
	def foo_view():
		return render_template("foo.html")
	
	return {
		"index": index_view,
		"foo": foo_view
	}