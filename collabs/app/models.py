# models.py

from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    rating = models.FloatField()
    platform = models.CharField(max_length=50, choices=[
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok'),
        ('User Generated Content', 'User Generated Content')
    ])

    def __str__(self):
        return self.name

class Content(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
