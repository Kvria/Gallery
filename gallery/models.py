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
    photos = models.ImageField(upload_to= 'images/')
    image_id = models.IntegerField(primary_key = True)
    image_name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
    Image.objects.filter(pk=self.id).delete()

    @classmethod
    def display_all_images(cls):
        images = cls.objects.all()
        return images

     @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def filter_by_location(cls,location_term):
        locations = cls.objects.filter(location__i_location__icontains=location_term)
        return locations

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__i_category__icontains=search_term)
        return images

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id = id).update(name = value)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Category(models.Model):
    category_id = models.IntegerField(primary_key = True)
    category_name = models.CharField(max_length = 45)

