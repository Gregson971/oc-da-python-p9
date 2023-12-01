from django.contrib.auth.models import AbstractUser, Group
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
    follows = models.ManyToManyField(
        "self", limit_choices_to={'role': CREATOR}, symmetrical=False, verbose_name="suit"
    )

    def assign_permissions(self):
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.assign_permissions()
