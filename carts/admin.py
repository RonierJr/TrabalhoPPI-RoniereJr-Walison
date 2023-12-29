from django.contrib import admin
from .models import Pedido

# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display= ('usuario','data_pedido')