import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from .models import University, Author

@shared_task
def create_random_user_accounts():
    while True:
        print("qwwe")
    return 1