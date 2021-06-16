from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('home/', views.home, name='app-home'),
    path('index/', views.index, name='second-page')
]