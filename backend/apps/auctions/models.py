from django.db import models

from apps.base.models import AuditModel
from apps.users.models import Person


class Offer(AuditModel):
    """ Model for offers """

    class AmountType(models.TextChoices):
        TON = 'TON', 'Toneladas'
        KG  = 'KG', 'Kilos'

    customer = models.ForeignKey(
        Person, 
        verbose_name='Ofertante',
        on_delete=models.CASCADE, 
        related_name='offers'
    )
    location_from   = models.CharField(verbose_name='De', max_length=200)
    location_to     = models.CharField(verbose_name='Para', max_length=200)
    initial_value   = models.DecimalField(verbose_name='Valor inicial', max_digits=20, decimal_places=2)
    amount          = models.DecimalField(verbose_name='Quantidade', max_digits=20, decimal_places=2)
    amount_type     = models.CharField(verbose_name="Tipo", max_length=3, choices=AmountType.choices)

    def __str__(self) -> str:
        return f'{self.pk}: {self.location_from} a {self.location_to}'


class Bid(models.Model):
    """ Model to bids """

    provider = models.ForeignKey(
        Person, 
        verbose_name='Fornecedor',
        on_delete=models.CASCADE, 
        related_name='bids'
    )
    offer = models.ForeignKey(
        Offer, 
        verbose_name='Ofertante',
        on_delete=models.CASCADE, 
        related_name='bids'
    )
    value   = models.DecimalField(verbose_name='Valor', max_digits=20, decimal_places=2)
    amount  = models.DecimalField(verbose_name='Quantidade', max_digits=20, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.provider} - {self.offer}'
