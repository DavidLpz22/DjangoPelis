from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Participante(models.Model): 
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    recomendado_por = models.ForeignKey(Participante, on_delete=models.SET_NULL, null=True)
    calificacion = models.FloatField(default=0)
    def __str__(self):
        return self.titulo