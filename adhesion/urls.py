from django.urls import path

from .views import accueil, merci

urlpatterns = [

    path(
        '',
        accueil,
        name='accueil'
    ),

    path(
        'merci/',
        merci,
        name='merci'
    ),

]