from django.contrib import admin
from .models import Marca, Tenis

# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display= ('nome',)

@admin.register(Tenis)
class TenisAdmin(admin.ModelAdmin):
    list_display= ('nome','marca','valor',)