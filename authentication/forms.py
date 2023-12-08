from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    '''
    Form for signing up a new user.
    '''

    # Define profile_photo field as an ImageField with required=False
    profile_photo = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        '''
        Meta class for SignupForm.

        Attributes:
            model (User): The user model.
            fields (tuple): The fields to display in the form.
        '''

        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name", "profile_photo")
