from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                )
            },
        ),
    )
    readonly_fields = ('last_login', 'date_joined', 'updated_at')
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('password1', 'password2',),
            },
        ),
    )
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'date_joined',
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-id',)


admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
