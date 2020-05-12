from django.urls import path
from .views import *

urlpatterns = [
    path('edit/', edit_card, name='edit_card'),
    path('account/', account, name='account'),
]
