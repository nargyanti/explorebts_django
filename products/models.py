from email.mime import image
from django.db import models

# Create your models here.
class product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.IntegerField()