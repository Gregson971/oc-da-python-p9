from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_writter_display(context, user):
    if user == context['user']:
        return 'vous'
    else:
        return user.username
