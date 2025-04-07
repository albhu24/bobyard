from django.urls import path
from db import views

urlpatterns = [
    path('comments/', views.comments, name='comments'),
]