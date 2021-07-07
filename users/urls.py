from django.urls import path
from .views import create_group, student_join_group

urlpatterns = [
    path('create_group/', create_group, name='create-group'),
    path('join_group/', student_join_group, name='join-group')
]