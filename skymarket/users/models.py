from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    USER = 'user', _('Пользователь')
    ADMIN = 'admin', _('Админ')

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=70, null=False)
    last_name = models.CharField(max_length=70, null=False)
    phone = PhoneNumberField(null=False, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default='user')
    image = models.ImageField(upload_to="photos/", verbose_name="фото", null=True, blank=True,)
    is_active = models.BooleanField(default=True, verbose_name='Аккаунт активен')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone',
    ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email
