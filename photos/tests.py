from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.

class CategoryTest(TestCase):
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def setUp(self):
        self.travel = Category(category_name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel, Category))

    def test_save_method(self):
        self.travel.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.travel.save_category()
        self.travel.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update_method(self):
        self.travel.save_category()
        self.travel.update_category(self.travel.id, 'cars')
        category = Category.objects.filter(category_name='cars')
        self.assertTrue(len(category) == 1)