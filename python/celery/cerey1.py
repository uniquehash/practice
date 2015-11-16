from celery import Celery

app = Celery('cerey1', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
	return x + y
