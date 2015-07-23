import sqlite3
import json

def initialize_db_json(filename):
    data = json.load(filename)
    if "name" in data:
        name = data[name]
    else:
        i = 1
        while os.getcwd()+"/"+"class"+str(i) in os.listdir():
            pass 
