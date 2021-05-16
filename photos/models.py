from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Location(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Image(models.Model):
    image = models.ImageField(upload_to='pictures/', null=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)