from django.db import models
from django.utils.translation import gettext_lazy as _


class Tea(models.Model):
    class TeaTypes(models.TextChoices):
        GREEN = 'GREEN', _('Zielona')
        WHITE = 'WHITE', _('Biała')
        BLACK = 'BLACK', _('Czarna')
        RED = 'RED', _('Czerwona')

    tea_name = models.CharField(max_length=100, default='')
    tea_type = models.CharField(choices=TeaTypes.choices, max_length=10)

    def __str__(self):
        return '{ id: ' + str(self.pk) + ', name: ' + self.tea_name + ' }'

    def serialize(self):
        return {
            "id": self.pk,
            "teaName": self.tea_name,
            "teaType": dict(self.TeaTypes.choices).get(self.tea_type)
        }


class TeaDescription(models.Model):
    tea_ref = models.ForeignKey(Tea, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '{ teaRef: ' + str(getattr(self.tea_ref, 'pk')) + ', order: ' + str(self.order) + ', heading: ' + self.heading[0:20] + ' [...], description: ' + self.description[0:20] + ' [...] }'

    def serialize(self):
        return {
            'order': self.order,
            'header': self.heading,
            'description': self.description
        }


class TeaCharacteristics(models.Model):
    tea_ref = models.OneToOneField(Tea, on_delete=models.CASCADE)
    tea_amount = models.CharField(max_length=20)
    water_temp = models.IntegerField()
    steeping_time = models.IntegerField(
        verbose_name='Steeping time in minutes')
    amount_of_steeps = models.IntegerField()
    notes = models.CharField(max_length=100)

    def __str__(self):
        return '{ teaRef: ' + str(getattr(self.tea_ref, 'pk')) + ' }'

    def serialize(self):
        return {
            'teaAmount': self.tea_amount,
            'waterTemp': self.water_temp,
            'steepingTime': self.steeping_time,
            'amountOfSteeps': self.amount_of_steeps,
            'notes': self.notes
        }
