from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customuser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
