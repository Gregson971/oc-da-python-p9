from django.urls import path

from . import views

urlpatterns = [
    path('feed/', views.feed, name='home'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path('tickets/<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
    path('posts/', views.view_posts, name='view_posts'),
]
