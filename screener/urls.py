from django.urls import path
from . import views

urlpatterns = [
    path('screener/', views.screener, name='screener'),
    path('test/', views.test, name='test'),
]
