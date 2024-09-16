from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.fyp_login, name='fyp-login'),
    path('logout/', views.fyp_logout, name='fyp-logout'),
    path('register/', views.register, name='fyp-register'),
    path('profile/', views.profile, name='fyp-profile'),
    path('edit-profile/<int:pk>/', views.edit_profile, name='fyp-edit_profile'),
    path('funds/', views.add_funds, name='fyp-add_funds'),
]