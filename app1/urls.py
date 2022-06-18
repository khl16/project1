from django.urls import path 
from . import views
urlpatterns = [
    path('blogs/', views.index),
    path('blogs/new/', views.index2),
    path('blogs/<int:val>/', views.intr),
]
