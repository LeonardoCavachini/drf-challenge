import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class Propertie(models.Model):
    property_code = models.UUIDField(
        verbose_name=_('property code'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    limit_guests = models.IntegerField(
        verbose_name=_('guests limit'),
        null=True,
        blank=True,
    )
    bathroom_quantity = models.IntegerField(
        verbose_name=_('bathrooms quantity'),
        null=True,
        blank=True,
    )
    accept_animal = models.BooleanField(
        verbose_name=_('accept animals'),
        default=False,
    )
    housekeeping_price = models.FloatField(
        verbose_name=_('housekeeping price'),
        null=True,
        blank=True,
    )
    activate_date = models.DateField(
        verbose_name=_('activate date'),
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
        verbose_name=_('createdAt'),
    )
    update_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
        verbose_name=('updatedAt'),
    )
