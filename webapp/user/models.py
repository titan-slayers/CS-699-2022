from turtle import title
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Trending(models.Model):
    title = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=10)
    alink = models.CharField(max_length=500)
    flink = models.CharField(max_length=500)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} {self.timestamp}'

class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=10)
    alink = models.CharField(max_length=500)
    flink = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.user} {self.title} {self.timestamp}'

