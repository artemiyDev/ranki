from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('user/', UserView.as_view()),
    path('decks/', DeckView.as_view()),
    path('decks/create', DeckCreateView.as_view()),
    path('decks/delete', DeckDeleteView.as_view()),
    path('deck/', CardsView.as_view()),
    path('card/create', CardCreateView.as_view()),
    path('card/changedate', CardChangeRepeatDateView.as_view()),

]
