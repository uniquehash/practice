from flask_script import Manager
from flaskr import app

manager = Manager(app)

@manager.command
def hello():
	print "hello"

@manager.command
def initdb():
	app.initdb()

if __name__ == "__main__":
	manager.run()








