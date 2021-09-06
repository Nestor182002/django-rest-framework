from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# user
from django.conf import settings
User=settings.AUTH_USER_MODEL
# mail
from django.core.mail import send_mail

# Create your models here.
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# signals
@receiver(post_save, sender=User)
def RegisterUserMail(sender, instance, **kwargs):
    send_mail("Gracias por unirse","bienvenido a este proyecto",settings.EMAIL_HOST_USER,[instance.email],fail_silently=False)
    
