from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta raíz
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('asignar/', views.asignar_servicio, name='asignar_servicio'),
    path('asignaciones/', views.listar_asignaciones, name='listar_asignaciones'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('servicios/', views.listar_servicios, name='listar_servicios'),
]
