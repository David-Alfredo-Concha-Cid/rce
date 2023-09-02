from django.shortcuts import render, get_object_or_404, redirect
from config.forms import KinesiologoForm, DeportistaForm, TratamientoForm
from django.http import HttpResponseRedirect, Http404
from .models import Kinesiologo, Deportista, Tratamiento
from django.db import transaction


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
            return HttpResponseRedirect('/Deportista/list/depor')
    
    context1 = { 
        'form': DeportistaForm()
        
    }
    return render(request, "deportista_create.html", context1)




def deportista_listar(request):
    context = {
      'depor': Deportista.objects.all()
    }
    return render(request, "list_depor.html", context)


def depor_eliminar(request, deportista_id):
    cont = {
        'depor': Deportista.objects.get(id = deportista_id)
    }
    if request.method == 'POST':
        cont['depor'].delete()
        return HttpResponseRedirect('/Deportista/list/depor')
    
    return render(request, 'deportista_delete.html', cont)


def kine_eliminar(request, kinesiologo_id):
    kine = get_object_or_404(Kinesiologo, id=kinesiologo_id)
    
    if request.method == 'POST':
        # Desvincular los tratamientos del kinesiólogo
        tratamientos = kine.tratamiento_set.all()
        for tratamiento in tratamientos:
            tratamiento.kinesiologo = None
            tratamiento.save(update_fields=['kinesiologo'])
        
        # Ahora puedes eliminar el kinesiólogo
        kine.delete()
        return redirect('/kinesiologo/list/kine/')  # Cambia esto a la URL correcta
    
    context = {'kine': kine}
    return render(request, 'kinesiologo_delete.html', context)


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


def deportista_editar(request, deportista_id):
    try:
        context = {
            'depor': Deportista.objects.get(id = deportista_id), 
        }
        
    except:
        raise Http404 
    
    if request.method == 'POST': #if para actualizar datos ya creados
        form = DeportistaForm(request.POST, instance  = context['depor']) #para actualizar datos creados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Deportista/list/depor")
        

    #context ya existe
    context['form'] = DeportistaForm(instance = context['depor'])

    return render(request, 'deportista_editar.html', context)


def kinesiologo_editar(request, kinesiologo_id):
    try:
        context = {
            'kine': Kinesiologo.objects.get(id = kinesiologo_id), 
        }
        
    except:
        raise Http404 
    
    if request.method == 'POST': #if para actualizar datos ya creados
        form = KinesiologoForm(request.POST, instance  = context['kine']) #para actualizar datos creados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/kinesiologo/list/kine/")
        

    #context ya existe
    context['form'] = KinesiologoForm(instance = context['kine'])

    return render(request, 'kinesiologo_editar.html', context)




def estadistica(request):
    context = {}
    return render(request, "estadistica.html", context)
