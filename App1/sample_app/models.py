from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.username