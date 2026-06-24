from django.contrib import admin
from .models import Hardware, Software, Issue, Resolution

admin.site.register(Hardware)

admin.site.register(Software)

admin.site.register(Issue)

admin.site.register(Resolution)

# Register your models here.
