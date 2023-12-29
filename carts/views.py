from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho, ItemCarrinho,Pedido, ItemPedido
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from shoes.models import Tenis

@login_required
def adicionar_ao_carrinho(request, tenis_id):
    tenis = get_object_or_404(Tenis, id=tenis_id)

    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))

        if quantidade > 0:
            carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
            
            item, item_created = ItemCarrinho.objects.get_or_create(tenis=tenis, quantidade=quantidade)
            carrinho.items.add(item)

    return redirect('index')


@login_required
def remover_do_carrinho(request, tenis_id):
    tenis = Tenis.objects.get(id=tenis_id)

    carrinho = Carrinho.objects.get(usuario=request.user)
    
    itens_a_remover = ItemCarrinho.objects.filter(tenis=tenis)
    carrinho.items.remove(*itens_a_remover)
    
    return redirect('ver_carrinho')

@login_required
def ver_carrinho( request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    items = carrinho.items.all()
    for item in items:
        item.subtotal = item.calcular_subtotal()

    total = carrinho.calcular_total()

    return render(request, 'carrinho/ver_carrinho.html', {'items': items, 'total': total})

@login_required
def criar_pedido(request):
    # Obtém ou cria o carrinho do usuário
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    items = carrinho.items.all()

    # Cria um novo pedido
    pedido = Pedido.objects.create(usuario=request.user)

    # Adiciona cada item do carrinho ao pedido
    for item in items:
        ItemPedido.objects.create(pedido=pedido, tenis=item.tenis, quantidade=item.quantidade, preco_unitario=item.tenis.valor)

    # Calcula o total do pedido
    total_pedido = pedido.calcular_total()

    # Limpa o carrinho após criar o pedido (opcional, dependendo da lógica desejada)
    carrinho.items.clear()

    return pedido.id

@login_required
def criar_pedido_view(request):
    if request.method == 'POST':
        # Utilize a função utilitária para criar o pedido
        pedido_id = criar_pedido(request)

        # Redirecione para uma página de confirmação ou outra página desejada
        return redirect('pedido_confirmado', pedido_id=pedido_id)

    # Se o método não for POST, talvez você queira lidar de maneira diferente
    return redirect('ver_carrinho') 

@login_required
def pedido_confirmado(request, pedido_id):
    # Obtenha o pedido usando o ID fornecido
    pedido = get_object_or_404(Pedido, id=pedido_id)
    total_pedido = pedido.calcular_total()

    return render(request, 'carrinho/pedido_confirmado.html', {'pedido': pedido, 'total_pedido': total_pedido})

@login_required
def ver_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    total_pedido = pedido.calcular_total()

    return render(request, 'carrinho/ver_pedido.html', {'pedido': pedido, 'total_pedido': total_pedido})

@login_required
def ver_todos_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    
    return render(request, 'carrinho/ver_todos_pedidos.html', {'pedidos': pedidos})