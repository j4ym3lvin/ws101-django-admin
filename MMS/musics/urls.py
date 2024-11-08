from django.urls import path
from .import views


urlpatterns = [
    path('', views.main, name='main'),
    path('musics/', views.musics, name='musics'),
    path('musics/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]