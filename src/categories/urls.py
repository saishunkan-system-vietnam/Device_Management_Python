from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('get_categories/', views.get_category, name='get_categories'),
    path('delete/',views.delete, name='delete')
]
