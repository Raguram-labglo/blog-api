from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Comment(models.Model):

    commant_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comments')
    commant = models.TextField(null = True)

class Feed(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    comands = models.ManyToManyField(Comment)