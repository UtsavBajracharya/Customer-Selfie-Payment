from django.urls import path
from . import views

app_name = 'fyp'

urlpatterns = [
    path('home/<int:page>', views.home),
    path('', views.welcome, name='fyp-welcome'),
    path('home/search', views.search),
    
    
]
