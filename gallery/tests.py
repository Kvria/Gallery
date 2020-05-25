from django.test import TestCase
from .models import Editor

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

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Uploading a new image and saving it

        self.new_image= Image(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_image.save() 

    def tearDown(self):
        Editor.objects.all().delete()
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
