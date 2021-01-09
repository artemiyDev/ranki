from rest_framework.serializers import ModelSerializer
from ranki.models import Card, Deck
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class DeckSerializer(ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
