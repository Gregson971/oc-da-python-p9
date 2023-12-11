from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag(takes_context=True)
def get_writter_display(context, user):
    if user == context['user']:
        return 'créé par vous'
    else:
        return f'créé par {user.username}'


@register.simple_tag(takes_context=True)
def get_review_writter_display(context, user):
    if user == context['user']:
        return 'publié par vous'
    else:
        return f'publié par {user.username}'


@register.simple_tag
def star_rating(rating):
    return '★' * int(rating) + '☆' * (5 - int(rating))


@register.filter
def get_posted_at_display(date_created):
    # Si le post a été publié il y a entre 1 et 60 minutes, on affiche 'Posté il y a x minutes'
    # Si le post a été publié il y a entre 1 et 24h, on affiche 'Posté il y a x heures'
    # Sinon au-delà de 24h, on affiche 'Posté le jj/mm/aaaa à hh:mm'

    if date_created > timezone.now() - timezone.timedelta(seconds=60):
        seconds = (timezone.now() - date_created).seconds
        return f'il y a {seconds} secondes'
    if date_created > timezone.now() - timezone.timedelta(minutes=60):
        minutes = (timezone.now() - date_created).seconds // 60
        return f'il y a {minutes} minutes'
    elif date_created > timezone.now() - timezone.timedelta(hours=24):
        hours = (timezone.now() - date_created).seconds // 3600
        return f'il y a {hours} heures'
    else:
        return f'le {date_created.strftime("%d/%m/%Y à %H:%M")}'
