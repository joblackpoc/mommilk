from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('home', views.HomeView.as_view(), name='home'),
    path('<int:pk>/',views.PostView.as_view(),name='post'),
    path('search/',views.SearchView.as_view(),name='search'),
    path('tags/<int:id>/',views.Tags,name='tag'),
]
