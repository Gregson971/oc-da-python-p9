from django.contrib import admin

from authentication.models import User, UserFollows


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'role', 'profile_photo')


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


admin.site.register(User, UserAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
