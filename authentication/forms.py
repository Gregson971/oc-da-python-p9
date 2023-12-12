from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    '''
    Form for signing up a new user.
    '''

    class Meta(UserCreationForm.Meta):
        '''
        Meta class for SignupForm.

        Attributes:
            model (User): The user model.
            fields (tuple): The fields to display in the form.
        '''

        model = get_user_model()
        fields = ('username',)


class EditProfileForm(forms.ModelForm):
    '''
    Form for editing a user's profile.
    '''

    # Profile photo is optional
    profile_photo = forms.ImageField(required=False)

    class Meta:
        '''
        Meta class for EditProfileForm.

        Attributes:
            model (User): The user model.
            fields (tuple): The fields to display in the form.
        '''

        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_photo')
