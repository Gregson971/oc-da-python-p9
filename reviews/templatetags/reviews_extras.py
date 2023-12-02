from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_writter_display(context, user):
    if user == context['user']:
        return 'vous'
    else:
        return user.username


@register.simple_tag(takes_context=True)
def get_review_writter_display(context, user):
    if user == context['user']:
        return 'Vous avez publié une critique'
    else:
        return f'{user.username} a publié une critique'
