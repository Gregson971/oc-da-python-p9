from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from . import forms


def signup_page(request):
    '''
    View for the signup page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''

    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "authentication/signup.html", {"form": form})


def edit_profile(request):
    '''
    View for the edit profile page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''

    form = forms.EditProfileForm(instance=request.user)

    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, "authentication/edit_profile_done.html")

    return render(request, "authentication/edit_profile.html", {"form": form})


def logout_user(request):
    '''
    View for logging out a user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''

    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
