from django.urls import path
from . import views

urlpatterns = [
    path('', views.database_home, name='home'),
    path('add_unit', views.add_unit, name='add')
]