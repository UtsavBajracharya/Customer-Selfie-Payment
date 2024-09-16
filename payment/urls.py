from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('home/pay/<int:id>/', views.pay),
    path('view-payment/<int:page>/', views.view_payments, name="view_payments"),
    path('view-payment/search/', views.search),
]
