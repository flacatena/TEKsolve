from django.contrib import admin
from .models import Hardware, Software, Issue, Resolution

@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ['hardware_device','id','return_hardware_id']

    def return_hardware_id(self,obj):
        return obj.hardware_device.id if obj.hardware_device else '-'

admin.site.register(Software)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['reported_issue','pk','id','hardware_id']

    def hardware_id(self,obj):
        return obj.hardware.id if obj.hardware else '-'


@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):
    list_display = ['reported_resolution','id']



# Register your models here.
