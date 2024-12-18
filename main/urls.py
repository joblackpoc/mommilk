from django.urls import path
from . import views

import os
from django.conf import settings
from urllib.parse import urljoin
from django.core.files.storage import FileSystemStorage
class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""

    location = os.path.join(settings.MEDIA_ROOT, "django_ckeditor_5")
    base_url = urljoin(settings.MEDIA_URL, "django_ckeditor_5/")

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('post_list', views.post_list, name='post_list'),
    path('new/', views.create_post, name='create_post'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.update_post, name='update_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
]
