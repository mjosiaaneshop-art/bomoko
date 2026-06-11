from django import forms
from .models import Adherent


class AdherentForm(forms.ModelForm):

    class Meta:
        widgets = {
    'date_naissance': forms.DateInput(
        attrs={'type': 'date'}
    ),

    'motivation': forms.Textarea(
        attrs={'rows': 5}
    ),

    'adresse': forms.Textarea(
        attrs={'rows': 3}
    ),
}
        model = Adherent

        fields = [
            'nom',
            'post_nom',
            'prenom',
            'sexe',
            'lieu_naissance',
            'date_naissance',
            'adresse',
            'telephone',
            'email',
            'profession',
            'niveau_etude',
            'motivation',
            'adhesion_gratuite',
            'aucun_salaire',
            'contribution',
            'respect_valeurs',
            'developpement_communautaire',
            'declaration_finale'
        ]