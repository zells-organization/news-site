from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group

from news.library import USER_GROUP_NAME, ADMIN_GROUP_NAME, EDITOR_GROUP_NAME


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, group, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.groups.add(group)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        group = Group.objects.get(name=USER_GROUP_NAME)
        return self._create_user(email, password, group, **extra_fields)

    def create_editor(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        group = Group.objects.get(name=EDITOR_GROUP_NAME)

        return self._create_user(email, password, group, **extra_fields)

    def create_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser (admin) must have is_superuser=True')

        group = Group.objects.get(name=ADMIN_GROUP_NAME)
        return self._create_user(email, password, group, **extra_fields)
