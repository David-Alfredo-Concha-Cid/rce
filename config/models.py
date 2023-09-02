from django.db import models

class Kinesiologo(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Deportista(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    deporte = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    kinesiologo = models.ForeignKey(Kinesiologo, on_delete=models.SET_NULL, null=True)
    deportista = models.ForeignKey(Deportista, on_delete=models.SET_NULL, null=True)
    fecha_atencion = models.DateField()
    diagnostico = models.TextField(null=True)
    ejercicios = models.TextField(null=True)
    observaciones = models.TextField(null=True)
    
    def __str__(self):
        return f"Tratamiento de {self.kinesiologo} a {self.deportista} el {self.fecha_atencion}"
