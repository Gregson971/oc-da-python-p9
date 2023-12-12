from django import forms

from . import models


class TicketForm(forms.ModelForm):
    '''
    Form for creating a new ticket.

    Attributes:
        title (CharField): The title of the ticket.
        description (TextField): The description of the ticket.
        image (ImageField): The image of the ticket.
    '''

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(label="Titre", max_length=128, widget=forms.TextInput())
    description = forms.CharField(label="Description", max_length=2048, widget=forms.Textarea(), required=False)
    image = forms.ImageField(label="Image", required=False)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    '''
    Form for deleting a ticket.

    Attributes:
        delete_ticket (BooleanField): A boolean field that is used to delete a ticket.
    '''

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    '''
    Form for creating a new review.

    Attributes:
        headline (CharField): The headline of the review.
        rating (ChoiceField): The rating of the review.
        body (CharField): The body of the review.
    '''

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    headline = forms.CharField(label="Titre", max_length=128, widget=forms.TextInput())
    rating = forms.ChoiceField(
        initial=1,
        label="Rating",
        widget=forms.RadioSelect(),
        choices=((1, "1 star"), (2, "2 stars"), (3, "3 stars"), (4, "4 stars"), (5, '5 stars')),
    )
    body = forms.CharField(label="Critique", max_length=8192, widget=forms.Textarea(), required=False)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.Form):
    '''
    Form for deleting a review.

    Attributes:
        delete_review (BooleanField): A boolean field that is used to delete a review.
    '''

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.Form):
    '''
    Form for following users.

    Attributes:
        followed_user (CharField): The user to follow.
    '''

    followed_user = forms.CharField(label=False, widget=forms.TextInput())
