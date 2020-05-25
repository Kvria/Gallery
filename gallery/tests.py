from django.test import TestCase
from .models import Image,Location

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a location
        self.place = Location(location='Machakos')
        self.wapi.save_location()

        # Creating a category
        self.category = Category(category='cities')
        self.category.save_category()

        # Creating a new image and saving it
        self.image= Image(image_name = 'city lights', image_description= 'A photo of a busy city at night.',location= self.place, category=  self.category)
        self.image.save_image()

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Test Saving
    def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(photos)>0)

    # Test deleting
    def test_delete_method(self):
        self.image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(photos)<1)

    # Tests whether the image description is updated
    def test_update_image_description(self):
        
        self.image.save_image()
        self.image.update_image_description(self.image.id,'city')
        new_update = Image.objects.get(name = "image")
        self.assertEqual(new_update.description, 'city')

    # Tests whether image can be searched  by location
    def test_search_location(self):
        
        self.machakos.save_location()
        self.image.save_image()
        images = Image.filter_by_location("machakos")
        self.assertTrue(len(photos) > 0)

class LocationTestClass(TestCase):
 
    # Set up method
    def setUp(self):
        self.place = Location(location='Machakos')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    # Test Save method
    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.place.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<1)

    def tearDown(self):
        Location.objects.all().delete()

    # Tests whether the location name is updated
    def test_update_location(self):
        self.machakos.save_location()
        self.machakos.update_location(self.nairobi.id,'nairobi')
        new_update = Location.objects.get(name = "nairobi")
        self.assertEqual(new_update.name, 'nairobi')

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = Category(i_category='Landscape')
    