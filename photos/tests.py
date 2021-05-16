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


class LocationTest(TestCase):
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def setUp(self):
        self.nai = Location(city='Nairobi', country='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.nai, Location))

    def test_save_method(self):
        self.nai.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_method(self):
        self.nai.save_location()
        self.nai.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update_method(self):
        self.nai.save_location()
        self.nai.update_location(self.nai.id, 'Kampala', 'Uganda')
        location = Location.objects.filter(city='Kampala')
        self.assertTrue(len(location) == 1)