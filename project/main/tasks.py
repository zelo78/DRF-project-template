from app.celery import celery_app

# Декоратор @app.task, говорит celery о том, что эта функция является (task-ом) т.е. должна выполнятся в фоне.
@celery_app.task
def supper_sum(x, y):
    return x + y
