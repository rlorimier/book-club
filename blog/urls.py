from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.details, name='details'),
    path('post/new/', views.newpost, name='newpost'),
    path('post/<int:pk>/edit/', views.newpost, name='newpost'),
    path('post/about', views.about, name='about'),
]
