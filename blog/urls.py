#importing django function path and all views from the blog application
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name ='post_list'),
]


