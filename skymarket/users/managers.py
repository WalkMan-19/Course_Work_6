from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None, role='user'):
        """
        Метод создаёт пользователя
        """
        if email:
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=password,
                role=role,
            )
            user.set_password(password)
            user.is_active = True
            user.save()
            return user
        else:
            raise ValueError('email field is required')

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """Метод создаст суперпользователя"""
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role='admin',
        )
        user.save()
        return user
