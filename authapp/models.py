from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            return ValueError(_("Email should be provided"))
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()




class User(AbstractUser):
    username = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=30,unique=True)
    phone_number = PhoneNumberField()

#    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
