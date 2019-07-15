from django.urls import path
from . import views

app_name = 'brand'
urlpatterns = [
    path('', views.brand, name='index'),
    path('/add', views.add_brand, name='add'),
]
