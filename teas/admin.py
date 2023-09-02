from django.contrib import admin

from .models import Tea, TeaCharacteristics, TeaDescription

admin.site.register([Tea, TeaDescription, TeaCharacteristics])

# Register your models here.
