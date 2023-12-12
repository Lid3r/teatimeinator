from django.contrib.auth.models import User
from django.db import models


class Fren(models.Model):
    REQUIRED_FIELDS = ('user',)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_host = models.BooleanField(default=False)

    def __str__(self) -> str:
        return super().__str__() + f" {self.is_host}"
