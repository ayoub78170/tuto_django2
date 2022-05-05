
from datetime import time
from django.utils import timezone
from django.db import models


# Create your models here.
class User(models.Model):
    nom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, default='')
    date_create = models.DateTimeField('date de creation',default=timezone.now)