from django.db import models
import uuid
import datetime
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500, blank=False)
    content= models.TextField(max_length=5000, blank=True)
    image= models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.Title