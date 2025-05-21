from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre  # Nombre para mostrar

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    usuarios = models.ManyToManyField(
        Usuario,
        through='AsignacionServicio',
        through_fields=('servicio', 'usuario')
    )

    def __str__(self):
        return self.nombre  

class AsignacionServicio(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('E', 'En proceso'),
        ('C', 'Completado'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
