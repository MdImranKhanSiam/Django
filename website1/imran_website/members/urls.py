from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_func, name='homepage'),
    path('members/', views.members_func, name='members'),
    path('members/details/<int:id>', views.details_func, name='Details'),
    path('details/<int:id>', views.details_func, name='Details')
]
