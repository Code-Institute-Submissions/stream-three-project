# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


# Create your models here.
class AccountUserManager(UserManager):
    def create_user(self, first_name, last_name, username, email, password,
                     is_staff, is_superuser, **extra_fields):

        # Creates and saves a User with the given username, email and password
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name,
                          username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    objects = AccountUserManager()

    def is_subscribed(self, postcard):
        try:
            purchase = self.purchases.get(postcard__pk=postcard.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True
