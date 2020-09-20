from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=150)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.headline

