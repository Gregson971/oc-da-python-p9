from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Value, CharField

from itertools import chain

from . import forms
from . import models


@login_required
def feed(request):
    # returns queryset of reviews for users followed by the current user
    followed_users = request.user.follows.all()
    reviews = models.Review.objects.filter(user__in=followed_users).order_by('-time_created')
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # returns queryset of tickets for users followed by the current user
    tickets = models.Ticket.objects.filter(user__in=followed_users).order_by('-time_created')
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    return render(request, 'reviews/feed.html', context={'posts': posts})


@login_required
def view_posts(request):
    print(request.user.get_all_permissions())
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
            return redirect('home')

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
                return redirect('home')

    context = {
        'delete_form': delete_form,
        'ticket': ticket,
    }

    return render(request, 'reviews/delete_ticket.html', context=context)
