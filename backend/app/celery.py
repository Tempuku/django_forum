import os
from celery import Celery
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

app = Celery('app', backend='redis', broker='redis://{}:6379/1'.format(REDIS_HOST))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.now = timezone.now

