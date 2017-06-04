from django.contrib import admin
from .models import Cuento


@admin.register(Cuento)
class CuentoAdmin(admin.ModelAdmin):
    model = Cuento
    list_display = ('title', 'active', 'created_at')
    search_fields = ['title']
