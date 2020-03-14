from django.db import models
from datetime import datetime
# Create your models here.

class Credential(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    timestamp = models.DateTimeField(default = datetime.utcnow)

    def __str__(self):
        return self.username
