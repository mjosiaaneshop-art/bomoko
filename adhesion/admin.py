from django.contrib import admin
from .models import Adherent


@admin.register(Adherent)
class AdherentAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'post_nom',
        'prenom',
        'telephone',
        'profession',
        'statut',
        'date_creation'
    )

    search_fields = (
        'nom',
        'post_nom',
        'prenom',
        'telephone'
    )

    list_filter = (
        'statut',
        'sexe',
        'date_creation'
    )

    list_editable = (
        'statut',
    )

    ordering = (
        '-date_creation',
    )