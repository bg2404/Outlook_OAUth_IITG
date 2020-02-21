from django.contrib import admin
from . import models


class JuntaAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(models.Junta, JuntaAdmin)
