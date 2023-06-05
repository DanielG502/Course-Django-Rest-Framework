from django.db import models
from django.contrib.auth.models import AbstractUser

#cambiamos el tipo de inicio de sesion, en vez de ID se usa ahora EMail
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []