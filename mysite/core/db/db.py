from os import path
import json
FILE_ROOT = path.abspath(path.dirname(__file__))

DB_SETTINGS_FILE = path.join(FILE_ROOT, 'dbsettings.json')


def get_product_dbsetting():
	with open(DB_SETTINGS_FILE,'r') as f:
		database_dict = json.load(f)
		return database_dict

class DatabaseDict():

	def __init__(self):
		with open(DB_SETTINGS_FILE,'r') as f:
			database_dict = json.load(f)
		self.database_dict = database_dict

d = DatabaseDict()