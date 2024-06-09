from django.db import models

# Create your models here.

class Message(models.Model):
    question = models.TextField()
    answer = models.TextField()
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
