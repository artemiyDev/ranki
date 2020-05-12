from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Card, Deck


def edit_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        print(request.user.id)
        if form.is_valid():
            bound_form = form.save(commit=False)
            bound_form.author_id = request.user.id
            bound_form.save()
            return redirect('edit_card')
    else:
        form = CardForm()
        return render(request, 'ranki/edit_card.html', {'form': form})


def account(request):
    decks_number = Deck.objects.filter(author=request.user).count()
    cards_number = Card.objects.filter(author=request.user).count()
    return render(request, 'ranki/account.html', {'cards_number': cards_number, 'decks_number': decks_number})
