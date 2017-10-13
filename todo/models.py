from django.db import models

# Create your models here.

class User (models.Model):
    username = models.EmailField(primary_key=True)
    password = models.CharField(max_length=32)


class Task (models.Model):
    username = models.EmailField() 
    description = models.CharField(max_length=256)
    status = models.CharField(max_length=32,default='TODO')
    start = models.DateTimeField(blank=True, null=True )
    expire = models.DateTimeField(blank=True, null=True )
    down = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, default=0)

