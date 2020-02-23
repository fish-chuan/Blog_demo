from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.


class Artical(models.Model):
    title = models.CharField(max_length=20, default="title")
    content = models.CharField(max_length=50, default="content")
    auth = models.CharField(max_length=20, default="user")
    img = models.ImageField(upload_to="article_pics")
    create_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)


class Like_Artical(models.Model):
    user = models.CharField(max_length=20, default="user")
    post = models.IntegerField(default=0)
