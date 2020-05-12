from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=160, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    repeat_date = models.DateField(auto_now_add=True)
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.question
