from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from user.models import Fren


class FrenInline(admin.StackedInline):
    model = Fren
    can_delete = False
    verbose_name_plural = 'Frens'


class FrenAdmin(UserAdmin):
    inlines = (FrenInline, )


admin.site.unregister(User)
admin.site.register(User, FrenAdmin)
# Register your models here.
