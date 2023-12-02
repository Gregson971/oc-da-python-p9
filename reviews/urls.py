from django.urls import path

from . import views

urlpatterns = [
    path('feed/', views.feed, name='home'),
    path('posts/', views.view_posts, name='view_posts'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path('tickets/<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
    path('tickets/<int:ticket_id>/reviews/create', views.create_ticket_review, name='create_ticket_review'),
    path('tickets/<int:ticket_id>/reviews/<int:review_id>/edit/', views.edit_ticket_review, name='edit_ticket_review'),
    path(
        'tickets/<int:ticket_id>/reviews/<int:review_id>/delete/',
        views.delete_ticket_review,
        name='delete_ticket_review',
    ),
    path('tickets-reviews/create/', views.create_ticket_and_review, name='create_ticket_and_review'),
]
