import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

OLAMA_URL = os.environ.get("OLAMA_URL")
DATABASE_PASSWORD = os.environ.get("MODELO")