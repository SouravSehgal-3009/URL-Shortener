from pyexpat import model
from django.db import models

# Create your models here.
class ShortURL(models.Model):
    longurl=models.URLField(max_length=1000)
    shorturl=models.CharField(max_length=100)
    date_time=models.DateTimeField()

    def __str__(self):
        return self.longurl