from django.urls import path
from . import views

app_name = 'device'
urlpatterns = [
    path('', views.index, name='index')
]
