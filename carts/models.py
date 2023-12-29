
from django.db import models
from shoes.models import Tenis
from django.contrib.auth import get_user_model

class ItemCarrinho(models.Model):
    tenis = models.ForeignKey(Tenis, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def calcular_subtotal(self):
        return self.tenis.valor * self.quantidade

class Carrinho(models.Model):
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemCarrinho)

    def calcular_total(self):
        return sum(item.tenis.valor * item.quantidade for item in self.items.all())
    
class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('em_processamento', 'Em Processamento'),
        ('concluido', 'Concluído'),
    )

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def calcular_total(self):
        return sum(item.tenis.valor * item.quantidade for item in self.items.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    tenis = models.ForeignKey(Tenis, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario