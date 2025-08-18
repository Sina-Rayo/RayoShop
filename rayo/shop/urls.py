from django.contrib import admin
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('' , views.main_shop , name="main"),
    path('create' , views.create_item , name='create'),
    path('sml<slug>' , views.small_categorie , name="sml"),
    path('big<slug>' , views.big_categorie , name="big"),
    path('<slug>', views.item_page),
]
