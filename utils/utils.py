from os import getenv

from dotenv import load_dotenv

def setup_environment():
	env: str | None = getenv("ENV")

	if env == "DEV":
		print("Development environment detected!\nLoading dotenv...")
		load_dotenv()

def get_env_string(env: str) -> str:
	temp: str | None = getenv(env)

	if temp == None:
		return ""
	
	return temp