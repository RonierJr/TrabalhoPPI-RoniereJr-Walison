from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django_filters.views import FilterView
from .filters import TenisFilter
from .models import Tenis, Marca
from carts.models import Pedido
from .forms import TenisForm, MarcaForm, PedidoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class IndexHomeView(FilterView):
    model = Tenis
    template_name = "tenis/index.html"
    filterset_class = TenisFilter
    ordering = ["-nome"]
    paginate_by = 8

    
class TenisDetailView( generic.DetailView):
    model = Tenis
    template_name = "tenis/detalhe.html" 

class TenisListView(GerentePermission, LoginRequiredMixin, generic.ListView):
    model = Tenis
    template_name = "admin-tenis/lista.html"
    paginate_by = 5

class TenisDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
    model = Tenis
    success_url = reverse_lazy("tenis_listar")
    success_message = "Tenis excluído com sucesso!"

class TenisCreateView(GerentePermission, LoginRequiredMixin, generic.CreateView):
    model = Tenis
    form_class = TenisForm
    success_url = reverse_lazy("tenis_listar")
    template_name = "admin-tenis/form.html"
    success_message = "Reserva cadastrada com sucesso!"
    error_message = "Erro ao cadastrar!"

    def form_valid(self, form):
        messages.success(self.request, "O Tenis foi cadastrada com sucesso")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

class TenisUpdateView(GerentePermission, LoginRequiredMixin,generic.UpdateView):
    model = Tenis
    form_class = TenisForm
    success_url = reverse_lazy("tenis_listar")
    template_name = "admin-tenis/form.html"

    def form_valid(self, form):
        messages.success(self.request, "O tenis foi atualizada com sucesso")
        return super().form_valid(form)

class MarcaListView(GerentePermission, LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "admin-marca/lista.html"
    paginate_by = 3

class MarcaCreateView(GerentePermission, LoginRequiredMixin, generic.CreateView):
    model = Marca
    form_class = MarcaForm
    success_url = reverse_lazy("marca_listar")
    template_name = "admin-marca/form.html"
    success_message = "Reserva cadastrada com sucesso!"
    error_message = "Erro ao cadastrar!"

    def form_valid(self, form):
        messages.success(self.request, "A marca foi cadastrada com sucesso")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class MarcaDeleteView(GerentePermission, LoginRequiredMixin,generic.DeleteView):
    model = Marca
    success_url = reverse_lazy("marca_listar")
    success_message = "Marca excluído com sucesso!"

class MarcaUpdateView(GerentePermission, LoginRequiredMixin,generic.UpdateView):
    model = Marca
    form_class = MarcaForm
    success_url = reverse_lazy("marca_listar")
    template_name = "admin-marca/form.html"

    def form_valid(self, form):
        messages.success(self.request, "A Marca foi atualizada com sucesso")
        return super().form_valid(form)
    
class AdmHomeView(GerentePermission,LoginRequiredMixin, generic.TemplateView):
    template_name = "tenis/administracao.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tenis"] = Tenis.objects.count()
        context["total_marca"] = Marca.objects.count()
        context["total_pedido"] = Pedido.objects.count()
        return context
    
class PedidoListView(GerentePermission, LoginRequiredMixin, generic.ListView):
    model = Pedido
    template_name = "admin-pedido/lista.html"
    paginate_by = 5

class PedidoDeleteView(GerentePermission,LoginRequiredMixin, generic.DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    success_message = "Pedido excluído com sucesso!"

class PedidoUpdateView(GerentePermission,LoginRequiredMixin, generic.UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy("pedido_lista")
    template_name = "admin-pedido/form.html"

    def form_valid(self, form):
        messages.success(self.request, "O Pedido foi atualizada com sucesso")
        return super().form_valid(form)
    
def quick_logout(request):
    logout(request)
    return redirect('index')

