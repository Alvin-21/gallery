from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, new_category):
        cls.objects.filter(id=id).update(category_name=new_category)

class Location(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city + ', ' + self.country

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, new_city, new_country):
        cls.objects.filter(id=id).update(city=new_city, country=new_country)

class Image(models.Model):
    image = models.ImageField(upload_to='pictures/', null=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__category_name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, city):
        images = cls.objects.filter(location__city__icontains=city)
        return images