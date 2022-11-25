import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models

from anuncios.models import Ad


# Create your models here.
class Reservation(models.Model):
    reservation_code = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        verbose_name=_('reservation code'),
        editable=False)
    ads_code = models.ForeignKey(
        Ad,
        verbose_name=_('ads code'),
        on_delete=models.CASCADE
    )
    guests = models.IntegerField(
        verbose_name=_('number of guests'),
        null=True,
        blank=True,
    )
    comments = models.TextField(
        verbose_name=_('comments'),
        null=True,
        blank=True,
    )
    total_price = models.FloatField(
        verbose_name=_('total price'),
        null=True,
        blank=True,
    )
    check_in = models.DateField(
        verbose_name=_('check-in'),
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        verbose_name=_('check-out'),
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
