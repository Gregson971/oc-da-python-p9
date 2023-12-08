from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from PIL import Image


class Review(models.Model):
    '''
    Model for a review.

    Attributes:
        headline (CharField): The headline of the review.
        body (TextField): The body of the review.
        rating (PositiveSmallIntegerField): The rating of the review.
        time_created (DateTimeField): The time the review was created.
        user (ForeignKey): The user who created the review.
        ticket (ForeignKey): The ticket the review is for.
    '''

    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)


class Ticket(models.Model):
    '''
    Model for a ticket.

    Attributes:
        title (CharField): The title of the ticket.
        description (TextField): The description of the ticket.
        image (ImageField): The image of the ticket.
        time_created (DateTimeField): The time the ticket was created.
        user (ForeignKey): The user who created the ticket.
    '''

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        img = Image.open(self.image.path)
        img.thumbnail(self.IMAGE_MAX_SIZE)
        # save of the resized image in the filesystem
        # this is not the save() method of the model !
        img.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
