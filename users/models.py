from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


from common.models import CreatedUpdatedAtMixin
from users.managers import CustomUserManager


class User(AbstractBaseUser, CreatedUpdatedAtMixin, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    first_name = models.CharField(blank=True, null=True, max_length=48)
    last_name = models.CharField(blank=True, null=True, max_length=48)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
