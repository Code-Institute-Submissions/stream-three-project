# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Postcard(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    imageTwo = models.ImageField(upload_to="images", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    postcard = models.ForeignKey(Postcard)
    subscription_end = models.DateTimeField(default=timezone.now)


from signals import subscription_created, subscription_was_cancelled
from paypal.standard.ipn.signals import valid_ipn_received


valid_ipn_received.connect(subscription_created)
valid_ipn_received.connect(subscription_was_cancelled)
