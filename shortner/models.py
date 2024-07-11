from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=6000)
    code = models.CharField(max_length=8)