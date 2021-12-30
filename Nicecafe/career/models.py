from django.db import models
from django.http import request

# Create your models here.
class Career(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=55)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.position