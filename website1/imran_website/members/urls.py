from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_func, name='members_func'),
]