from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email_address', max_length=255)
    message = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.full_name

class Subscription(models.Model):
    subscribed_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='email_address', max_length=255, unique=True)

    def __str__(self):
        return self.email