from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from custom import views
  
urlpatterns = [
    path('', views.home, name='home'),
    path('image_upload', convert_image_view, name = 'image_upload'),
    path('output', output, name = 'output'),
]
  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)