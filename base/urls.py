from django.urls import path
from .views import *

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
    path('rules/', rules, name='rules'),
    path('players/', players, name='players'),
    path('secret/', secret, name='secret'),
    path('clues/', clues, name='clues'),
    path('guess/', guess, name='guess'),
    path('notes/', notes, name='notes'),
    path('solve/', solve, name='solve'),
]

