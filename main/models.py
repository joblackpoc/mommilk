from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = CKEditor5Field(null=True, blank=True, config_name='extends')
    published_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    post_image = models.ImageField(upload_to='post',default='post/1.jpg')
    def __str__(self):
        return self.post_title
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)