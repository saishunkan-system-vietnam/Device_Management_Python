from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('<int:id>', views.edit, name='user_edit')
]
