from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members_func, name='members'),
    path('members/details/<int:id>', views.details_func, name='details'),
]
