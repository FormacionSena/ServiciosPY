from django.shortcuts import render, redirect
from .forms import UsuarioForm, ServicioForm, AsignacionServicioForm
from .models import AsignacionServicio, Usuario, Servicio

def home(request):
    return render(request, 'servicios/home.html')

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'servicios/crear_usuario.html', {'form': form})

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    else:
        form = ServicioForm()
    return render(request, 'servicios/crear_servicio.html', {'form': form})

def asignar_servicio(request):
    if request.method == 'POST':
        form = AsignacionServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_asignaciones')
    else:
        form = AsignacionServicioForm()
    return render(request, 'servicios/asignar_servicio.html', {'form': form})

def listar_asignaciones(request):
    asignaciones = AsignacionServicio.objects.all()
    return render(request, 'servicios/listar_asignaciones.html', {'asignaciones': asignaciones})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'servicios/listar_usuarios.html', {'usuarios': usuarios})

def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/listar_servicios.html', {'servicios': servicios})