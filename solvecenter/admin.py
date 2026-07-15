from django.contrib import admin
from .models import Hardware, Software, Issue, Resolution
from . forms import IssueForm

@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ['hardware_device','id']

admin.site.register(Software)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['reported_issue','hardware','software','pk','id']
    form = IssueForm

@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):
    list_display = ['reported_resolution','pk']




