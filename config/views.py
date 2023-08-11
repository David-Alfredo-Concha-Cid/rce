from django.shortcuts import render
from config.forms import KinesiologoForm, DeportistaForm, TratamientoForm
from django.http import HttpResponseRedirect, Http404
from .models import Kinesiologo, Deportista, Tratamiento


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def kinesiologo_create(request):
    if request.method == 'POST':
        form = KinesiologoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = { 
        'form': KinesiologoForm()
        
    }
    return render(request, "kinesiologo_create.html", context)


def kinesiologo_listar(request):
    context = {
      'kine': Kinesiologo.objects.all()
    }
    return render(request, "list_kine.html", context)


def deportista_create(request):
    if request.method == 'POST':
        form = DeportistaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    context1 = { 
        'form': DeportistaForm()
        
    }
    return render(request, "deportista_create.html", context1)




def deportista_listar(request):
    context = {
      'depor': Deportista.objects.all()
    }
    return render(request, "list_depor.html", context)




def atencion_create(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context2 = {
        'form': TratamientoForm()
    }
    return render(request, "atencion_create.html", context2)




def tratamiento_listar(request):
    context = {
      'aten': Tratamiento.objects.all()
    }
    return render(request, "list_aten.html", context)

