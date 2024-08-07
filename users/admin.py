from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка юзера"""
    list_display = (
        'id',
        'email',
        'phone',
        'token',
        'chat_id',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
