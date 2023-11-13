from django.contrib import admin
from django.urls import path, register_converter

from main_application import views, converters

app_name = 'main_application'
register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("home/", views.MainPageView.as_view(), name="home_page"),
    path("categories/<str:type_id>/", views.CategoriesView.as_view(), name="categories"),
    path("categories/<str:type_id>/<yyyy:year>/", views.CategoriesView.as_view(), name="categories"),
]
