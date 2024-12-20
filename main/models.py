import uuid

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.fields.related import ForeignKey

from django.urls import reverse
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    post_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=60)
    post_content = CKEditor5Field(null=True, blank=True, config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='post',default='post/1.jpg')


    def __str__(self):
        return self.post_title
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)