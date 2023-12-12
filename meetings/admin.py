from django.contrib import admin
from .models import Meeting, TeaChoices


class MeetingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date', 'title']


class TeaChoicesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'meeting_ref', 'person', 'tea_ref']


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(TeaChoices, TeaChoicesAdmin)

# Register your models here.
