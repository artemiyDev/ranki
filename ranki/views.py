import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Card, Deck
from .serializers import UserSerializer, DeckSerializer, CardSerializer
from django.contrib.auth.models import User
from rest_framework import status
from .date_calculator_service import calculateNextRepeatDate


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class DeckView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Deck.objects.filter(author=request.user.id)
        serializer = DeckSerializer(queryset, many=True)
        return Response(serializer.data)


class DeckCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        new_deck = Deck.objects.create(
            name=request.data['name'],
            description="",
            author_id=request.user.id)
        new_deck.save()
        return Response(status=status.HTTP_201_CREATED)


class DeckDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        print(request.data)
        deck = Deck.objects.get(id=request.data['deck_id'])
        if deck:
            deck.delete()
            return JsonResponse({"status": "ok"}, status=status.HTTP_200_OK)
        return JsonResponse({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)


class CardsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        deck_id = self.request.query_params.get('deck_id')
        queryset = Card.objects.filter(author=request.user.id, deck_id=deck_id,repeat_date__lte=datetime.date.today())
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)


class CardCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.data)
        new_card = Card.objects.create(
            deck_id=request.data['deck_id'],
            question=request.data['question'],
            answer=request.data['answer'],
            author_id=request.user.id,
            image=None,
            is_published=True,
        )
        new_card.save()
        deck = Deck.objects.get(id=request.data['deck_id'])
        deck.total += 1
        deck.new += 1
        deck.save()
        return Response(status=status.HTTP_201_CREATED)

class CardChangeRepeatDateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.data)
        card = Card.objects.get(id=request.data['card_id'])
        newCardParams = calculateNextRepeatDate(answer_quality=request.data['answer_quality'],easiness=card.easiness,interval=card.interval,repetitions=card.repetitions)
        print(newCardParams)
        card.repeat_date = newCardParams['review_date']
        card.easiness = newCardParams['easiness']
        card.repetitions = newCardParams['repetitions']
        card.interval = newCardParams['interval']
        card.save()
        return Response(status=status.HTTP_200_OK)
