from django.shortcuts import render, redirect, get_object_or_404
from .models import Tenis, Marca
from .forms import TenisForm, MarcaForm
from .forms import TenisForm, MarcaForm
from .forms import TenisForm, MarcaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class IndexHomeView(generic.ListView):
    model = Tenis
    template_name = "tenis/index.html"
    paginate_by = 8

    
class TenisDetailView( generic.DetailView):
    model = Tenis
    template_name = "tenis/detalhe.html" 

class TenisListView( generic.ListView):
    model = Tenis
    template_name = "admin-tenis/lista.html"
    paginate_by = 5

class TenisDeleteView(generic.DeleteView):
    model = Tenis
    success_url = reverse_lazy("tenis_listar")
    success_message = "Tenis excluído com sucesso!"

class TenisCreateView( generic.CreateView):
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

class TenisUpdateView(generic.UpdateView):
    model = Tenis
    form_class = TenisForm
    success_url = reverse_lazy("tenis_listar")
    template_name = "admin-tenis/form.html"

    def form_valid(self, form):
        messages.success(self.request, "O tenis foi atualizada com sucesso")
        return super().form_valid(form)

class MarcaListView( generic.ListView):
    model = Marca
    template_name = "admin-marca/lista.html"
    paginate_by = 3

class MarcaCreateView( generic.CreateView):
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


class MarcaDeleteView(generic.DeleteView):
    model = Marca
    success_url = reverse_lazy("marca_listar")
    success_message = "Marca excluído com sucesso!"

class MarcaUpdateView(generic.UpdateView):
    model = Marca
    form_class = MarcaForm
    success_url = reverse_lazy("marca_listar")
    template_name = "admin-marca/form.html"

    def form_valid(self, form):
        messages.success(self.request, "A Marca foi atualizada com sucesso")
        return super().form_valid(form)
    
class AdmHomeView(generic.TemplateView):
    template_name = "tenis/administracao.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tenis"] = Tenis.objects.count()
        context["total_marca"] = Marca.objects.count()
        return context
    