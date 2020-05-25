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
    image_id = models.IntegerField(primary_key = True)
    image_name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 100)
    # location = models.ForeignKey('Location', on_delete=models.CASCADE)
    # category = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor)
    pub_date = models.DateTimeField(auto_now_add=True)
