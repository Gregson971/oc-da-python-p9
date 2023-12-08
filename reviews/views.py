from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.db.models import Value, CharField, Q

from itertools import chain

from authentication.models import User, UserFollows
from . import forms
from . import models


@login_required
def feed(request):
    # returns queryset of reviews for users followed by the current user
    followed_users = request.user.follows.all()
    reviews = models.Review.objects.filter(
        # the user who wrote the review is in the list of followed users
        Q(user__in=followed_users)
        |
        # the user who wrote the review is the current user
        Q(user=request.user)
    ).order_by('-time_created')
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # returns queryset of tickets for users followed by the current user
    tickets = models.Ticket.objects.filter(user__in=followed_users).order_by('-time_created')
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    # Dectect if a follows user has already reviewed a ticket
    for post in posts:
        if post.content_type == 'TICKET':
            post.has_reviewed = models.Review.objects.filter(Q(ticket=post)).exists()

    return render(request, 'reviews/feed.html', context={'posts': posts})


@login_required
def view_posts(request):
    # returns queryset of reviews
    reviews = models.Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # returns queryset of tickets
    tickets = models.Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    return render(request, 'reviews/posts.html', context={'posts': posts})


@login_required
@permission_required('reviews.add_ticket', raise_exception=True)
def create_ticket(request):
    ticket_form = forms.TicketForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('view_posts')

    context = {'ticket_form': ticket_form}

    return render(request, 'reviews/create_ticket.html', context=context)


@login_required
@permission_required('reviews.change_ticket', raise_exception=True)
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)

    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('view_posts')

    context = {'edit_form': edit_form}

    return render(request, 'reviews/edit_ticket.html', context=context)


@login_required
@permission_required('reviews.delete_ticket', raise_exception=True)
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    delete_form = forms.DeleteTicketForm()

    if request.method == 'POST':
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('view_posts')

    context = {
        'delete_form': delete_form,
        'ticket': ticket,
    }

    return render(request, 'reviews/delete_ticket.html', context=context)


@login_required
@permission_required('reviews.add_review', raise_exception=True)
def create_ticket_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('view_posts')

    context = {
        'review_form': review_form,
        'ticket': ticket,
    }

    return render(request, 'reviews/create_ticket_review.html', context=context)


@login_required
@permission_required('reviews.change_review', raise_exception=True)
def edit_ticket_review(request, ticket_id, review_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)

    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('view_posts')

    context = {
        'edit_form': edit_form,
        'ticket': ticket,
    }

    return render(request, 'reviews/edit_ticket_review.html', context=context)


@login_required
@permission_required('reviews.delete_review', raise_exception=True)
def delete_ticket_review(request, ticket_id, review_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review = get_object_or_404(models.Review, id=review_id)
    delete_form = forms.DeleteReviewForm()

    if request.method == 'POST':
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('view_posts')

    context = {
        'delete_form': delete_form,
        'ticket': ticket,
        'review': review,
    }

    return render(request, 'reviews/delete_ticket_review.html', context=context)


@login_required
@permission_required(['reviews.add_ticket', 'reviews.add_review'], raise_exception=True)
def create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('view_posts')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }

    return render(request, 'reviews/create_ticket_and_review.html', context=context)


@login_required
def follow_users(request):
    follow_form = forms.FollowUsersForm()

    if request.method == 'POST':
        follow_form = forms.FollowUsersForm(request.POST)

        if follow_form.is_valid():
            try:
                followed_user = User.objects.get(username=request.POST['followed_user'])
                if request.user == followed_user:
                    messages.error(request, 'You can\'t subscribe to yourself!')
                else:
                    try:
                        UserFollows.objects.create(user=request.user, followed_user=followed_user)
                        request.user.follows.add(followed_user)
                        messages.success(request, f'You are now following {followed_user}!')
                    except IntegrityError:
                        messages.error(request, f'You are already following {followed_user}!')

            except User.DoesNotExist:
                messages.error(request, f'The user {follow_form.data["followed_user"]} does not exist.')

    user_follows = request.user.follows.all()
    followed_by = UserFollows.objects.filter(followed_user=request.user).order_by('user')

    context = {
        'follow_form': follow_form,
        'followed_users': user_follows,
        'following_users': followed_by,
    }

    return render(request, 'reviews/follow_users.html', context=context)


@login_required
def unfollow_users(request, user_id):
    user = get_object_or_404(User, id=user_id)

    try:
        UserFollows.objects.get(user=request.user, followed_user=user).delete()
        request.user.follows.remove(user)
        messages.success(request, f'You have unfollowed {user}!')
    except UserFollows.DoesNotExist:
        messages.error(request, f'You are not following {user}!')

    return redirect('follow_users')
