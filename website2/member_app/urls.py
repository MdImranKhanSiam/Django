from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_func, name='homepage'),
    path('members/', views.members_func, name='members'),
    path('members/details/<slug:slug>', views.details_func, name='Details'),
    path('testing/', views.testing_func, name='Testing'),
]
