from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.CharField(max_length=50)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
