from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login

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


def upload_profile_picture(request):
    form = forms.UploadProfilePictureForm(instance=request.user)

    if request.method == "POST":
        form = forms.UploadProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("upload_picture_done")

    return render(request, "authentication/upload_profile_picture.html", {"form": form})
