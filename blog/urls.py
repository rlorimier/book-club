from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.details, name='details'),
    path('', views.about, name='about'),
]
