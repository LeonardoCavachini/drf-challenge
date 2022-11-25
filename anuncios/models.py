from django.utils.translation import gettext_lazy as _
from django.db import models

from imoveis.models import Propertie


# Create your models here.
class Ad(models.Model):
    property_code = models.ForeignKey(
        Propertie,
        verbose_name=_('property code'),
        on_delete=models.CASCADE
    )
    platform_name = models.CharField(
        verbose_name=_('platform name'),
        max_length=128,
        null=True,
        blank=True,
    )
    platform_tax = models.FloatField(
        verbose_name=_('platform tax'),
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
