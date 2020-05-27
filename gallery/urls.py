from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^search/', views.search_results, name='search_category'),
    url('^location/', views.search_location, name='search_category')  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

