from django.contrib import admin

from reviews.models import Review, Ticket


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'time_created', 'user')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'user')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Ticket, TicketAdmin)
