from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexPage, name="index"),
    path('list/', views.PostList, name="list"),
    path('view/', views.PostView, name="view"),
    path('write/', views.PostWrite, name="write"),
    ]