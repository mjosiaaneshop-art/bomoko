from django.db import models


class Adherent(models.Model):

    STATUT_CHOICES = [
        ('ATTENTE', 'En attente'),
        ('ACCEPTE', 'Accepté'),
        ('REFUSE', 'Refusé'),
    ]

    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    nom = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    sexe = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES
    )

    lieu_naissance = models.CharField(max_length=150)

    date_naissance = models.DateField()

    adresse = models.TextField()

    telephone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
        null=True
    )

    profession = models.CharField(max_length=100)

    niveau_etude = models.CharField(max_length=100)

    motivation = models.TextField()

    adhesion_gratuite = models.BooleanField(default=False)

    aucun_salaire = models.BooleanField(default=False)

    contribution = models.BooleanField(default=False)

    respect_valeurs = models.BooleanField(default=False)

    developpement_communautaire = models.BooleanField(default=False)

    declaration_finale = models.BooleanField(default=False)

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='ATTENTE'
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nom} {self.post_nom}"