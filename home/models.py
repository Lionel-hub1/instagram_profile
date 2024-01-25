from django.db import models


class Profile(models.Model):
    names = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(
        upload_to="images/", default="images/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.names


class Post(models.Model):
    picture = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.picture.url
