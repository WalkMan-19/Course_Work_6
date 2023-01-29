# Generated by Django 3.2.6 on 2023-01-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Админ'), ("<class 'users.models.UserRoles.Meta'>", 'Meta')], default='user', max_length=50),
        ),
    ]
