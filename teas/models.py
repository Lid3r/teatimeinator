from django.db import models
from django.utils.translation import gettext_lazy as _


class Tea(models.Model):
    class TeaTypes(models.TextChoices):
        GREEN = 'GREEN', _('Zielona')
        WHITE = 'WHITE', _('Biała')
        BLACK = 'BLACK', _('Czarna')
        RED = 'RED', _('Czerwona')

    tea_name = models.CharField(max_length=100)
    tea_type = models.CharField(choices=TeaTypes.choices, max_length=10)

    def __str__(self):
        return self.tea_type


class TeaDescription(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class TeaCharacteristics(models.Model):
    tea = models.OneToOneField(Tea, on_delete=models.CASCADE)
    tea_amount = models.CharField(max_length=20)
    water_temp = models.IntegerField()
    steeping_time = models.IntegerField(verbose_name='Steeping time in minutes')
    amount_of_steeps = models.IntegerField()
    notes = models.CharField(max_length=100)
