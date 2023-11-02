from django.contrib import admin
from django.urls import path

from main_application import views

app_name = 'main_application'

urlpatterns = [
    path("home/", views.MainPageView.as_view(), name="home_page"),
    path("categories/", views.MainPageView.as_view(), name="categories"),
]
