from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1500, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ad')
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True)  # Просто в фикстурах объявлений было поле image

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
