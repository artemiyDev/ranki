from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=160,unique=True)
    description = models.CharField(max_length=160, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    due = models.IntegerField(default=0)
    new = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
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
    quality = models.IntegerField(default=1)
    easiness = models.FloatField(default=2.5)
    interval = models.IntegerField(default=1)
    repetitions = models.IntegerField(default=1)

    def __str__(self):
        return self.question
