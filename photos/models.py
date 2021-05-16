from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='pictures/', null=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    category_name = models.CharField(max_length=30)