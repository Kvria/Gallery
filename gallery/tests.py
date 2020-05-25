from django.test import TestCase
from .models import Editor,Image

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

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
 


        