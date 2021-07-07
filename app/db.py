from pysondb import db

# paths are absolute to project root
users = db.getDb("db/users.json")
todos = db.getDb("db/todos.json")