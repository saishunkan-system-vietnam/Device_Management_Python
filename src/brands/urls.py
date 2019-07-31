from django.urls import path
from . import views

app_name = 'brand'
urlpatterns = [
    path('', views.brand, name='index'),
    path('add', views.add, name='add'),
    path('chart', views.chart, name='chart'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete', views.delete, name='delete')
]
