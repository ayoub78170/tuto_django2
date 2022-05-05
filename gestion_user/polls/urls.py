from django.contrib import admin
from django.urls import include, path
from . import views
# /polls/
urlpatterns = [
    path('', views.index ,name ='index'),
    path('<int:user_id>/', views.detail , name='detail'),
]