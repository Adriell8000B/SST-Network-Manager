from flask import Blueprint, render_template

blueprint = Blueprint(
	"routes",
	__name__, 
	template_folder="../templates",
)

@blueprint.route("/")
def index():
	return render_template("index.html")

@blueprint.route("/foo")
def foo():
	return render_template("foo.html")