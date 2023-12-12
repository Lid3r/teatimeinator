from django.contrib import admin
from .models import Tea, TeaCharacteristics, TeaDescription


class TeaAdmin(admin.ModelAdmin):
    list_display = ["pk", "tea_name", "tea_type"]


class TeaDescriptionAdmin(admin.ModelAdmin):
    list_display = ["pk", "tea_ref", "order", "heading", "description"]


class TeaCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ["pk", "tea_ref", "tea_amount", "water_temp",
                    "steeping_time", "amount_of_steeps", "notes"]


admin.site.register(Tea, TeaAdmin)
admin.site.register(TeaDescription, TeaDescriptionAdmin)
admin.site.register(TeaCharacteristics, TeaCharacteristicsAdmin)


# Register your models here.
