from django.shortcuts import render
from base.models import *

# Example dynamic data
from datetime import date

# Tailwinds CSS homepage
def homepage(request):
    return render(request, 'base/homepage.html',)



def rules(request):
    return render(request, 'base/rules.html',)



def players(request):
    players = Characters.objects.all()

    return render(request, 'base/players.html', {
        'players': players,
    })



def secret(request):
    return render(request, 'base/secret.html',)



def clues(request):
    clues = Clues.objects.all()

    return render(request, 'base/clues.html', {
        'clues': clues,
    })



def guess(request):
    return render(request, 'base/guess.html',)



def notes(request):
    return render(request, 'base/notes.html',)



def solve(request):
    return render(request, 'base/solve.html',)



# Bootstrap Homepage
def bootstrap(request):

    this_year = date.today().year

    return render(request, 'bootstrap/bootstrap.html', context={
        'year': this_year,
    })