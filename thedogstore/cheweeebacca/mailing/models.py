from django.db import models
import requests

# Create your models here.


class Mailing(models.Model):
    dog = models.CharField(max_length=30)
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        unique_together = ['dog', 'email']
