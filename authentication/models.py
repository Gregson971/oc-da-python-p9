from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''
    User model for authentication.
    It is an extension of the AbstractUser model.
    It is used to store the user's profile photo and role.
    '''

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
