from django.contrib import admin
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('api' , views.api_main_page , name="api_main"),
    path('api/big/<slug>' , views.api_big_categorie , name="api_big"),
    path('api/sml/<slug>' , views.api_small_categorie , name="api_sml"),
    path('api/search/<slug>' , views.api_search , name='api_search'),
    path('api/create' , views.api_create_item , name='api_create'),
    path('api/signup' , views.api_signup , name='api_signup'),
    path('api/login' , views.api_login , name='api_login'),
    path('api/<slug>', views.api_item_page),

    path('' , views.main_shop , name="main"),
    path('create' , views.create_item , name='create'),
    path('sml<slug>' , views.small_categorie , name="sml"),
    path('big<slug>' , views.big_categorie , name="big"),
    path('<slug>', views.item_page),
    
]
