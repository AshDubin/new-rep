from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

celery_app = Celery(
    'blackglass',
    broker=os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    backend=os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0'),
)

celery_app.conf.task_routes = {"app.tasks.*": {"queue": "default"}}
