from django.shortcuts import render, redirect, get_object_or_404
from .models import Tenis, Marca
from .forms import TenisForm, MarcaForm

# Create your views here.
def index(request):
    teniss = Tenis.objects.all()
    context ={
       'teniss':teniss
    }
    return render(request, "tenis/index.html", context)

def detalhe_tenis(request,id_tenis):
    tenis = get_object_or_404(Tenis, id=id_tenis)
    context={
        'tenis':tenis,
    }
    return render(request,'tenis/detalhe.html',context)


def tenis_listar(request):
    teniss = Tenis.objects.all()
    context ={
        'teniss':teniss
    }
    return render(request, "admin-tenis/lista.html",context)

def tenis_remover(request, id):
    tenis = get_object_or_404(Tenis, id=id)
    tenis.delete()
    return redirect('tenis_listar') # procure um url com o nome 'lista_aluno'


def tenis_criar(request):
    if request.method == 'POST':
        form = TenisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = TenisForm()
    else:
        form = TenisForm()

    return render(request, 'admin-tenis/form.html', {'form': form})

def tenis_editar(request,id):
    tenis = get_object_or_404(Tenis,id=id)
   
    if request.method == 'POST':
        form = TenisForm(request.POST, request.FILES, instance=tenis)

        if form.is_valid():
            form.save()
            return redirect('tenis_listar')
    else:
        form = TenisForm(instance=tenis)

    return render(request,'admin-tenis/form.html',{'form':form})


def marca_listar(request):
    marcas = Marca.objects.all()
    context ={
        'marcas':marcas
    }
    return render(request, "admin-marca/lista.html",context)

def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca_listar')
    else:
        form = MarcaForm()

    return render(request, 'admin-marca/form.html', {'form': form})

def marca_remover(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('marca_listar')

def marca_editar(request,id):
    marca = get_object_or_404(Marca,id=id)
   
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)

        if form.is_valid():
            form.save()
            return redirect('marca_listar')
    else:
        form = MarcaForm(instance=marca)

    return render(request,'admin-marca/form.html',{'form':form})

def administracao(request):
    total_tenis = Tenis.objects.count()
    total_marca = Marca.objects.count()
    context = {
        'total_tenis' : total_tenis,
        'total_marca' : total_marca,
    }
    return render(request, "tenis/administracao.html",context)