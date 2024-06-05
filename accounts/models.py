#from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
 
class CustomUser(AbstractUser):
    is_received_email = models.BooleanField(verbose_name='お問い合わせメールを受け取るか', default=True)
 
    @staticmethod
    def get_users_emailed():
        return CustomUser.objects.filter(is_received_email=True)
 
    @staticmethod
    def email_users(users, subject, message, from_email=None):
        for user in users:
            user.email_user(subject, message, from_email)
