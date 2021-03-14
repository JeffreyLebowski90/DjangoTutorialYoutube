from django.contrib import admin
from .models import Roll

class RollAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Roll, RollAdmin)