from django.contrib import admin
from .models import Editor,Image,Location,Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
