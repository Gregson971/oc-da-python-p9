from django import forms

from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(label="Titre", max_length=128, widget=forms.TextInput())
    description = forms.CharField(label="Description", max_length=2048, widget=forms.Textarea(), required=False)
    image = forms.ImageField(label="Image", required=False)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
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
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.Form):
    followed_user = forms.CharField(label=False, widget=forms.TextInput())
