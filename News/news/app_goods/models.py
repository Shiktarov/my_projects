from django.db import models
from django.utils.translation import gettext_lazy as _
class Item(models.Model):
    code = models.CharField(max_length=100, verbose_name=_('Code'))
    #description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))

    class Meta:
        verbose_name_plural = _('goods')
        verbose_name = _('good')