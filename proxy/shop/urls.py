from django.urls import path

from .views import *

urlpatterns = [
    path('', shop),
    path('1/', add_to_cart),
]
