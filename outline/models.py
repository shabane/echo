from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=100)
    max_size = models.IntegerField(default=3000)
    usage = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)
    key = models.TextField()
    birth_date = models.DateField(auto_now_add=True)
    exp_date = models.DateField()


class Server(models.Model):
    certSha256 = models.TextField()
    apiUrl = models.CharField(max_length=255)
