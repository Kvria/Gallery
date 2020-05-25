from django.db import models

# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class Image(models.Model):
    image = models.ImageField(upload_to= 'images/')
    image_id = models.IntegerField(primary_key = True)
    image_name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey('location_id', on_delete=models.CASCADE)
    category = models.ForeignKey('category_id', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['image_name']

class Location(models.Model):
    location_id = models.IntegerField(primary_key = True)
    location_name = models.CharField(max_length = 30)

    

class Category(models.Model):
    category_id = models.IntegerField(primary_key = True)
    category_name = models.CharField(max_length = 45)

