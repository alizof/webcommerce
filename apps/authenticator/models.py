from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  cgc = models.CharField(max_length=18, blank=True, null=True)
