from django.db import models

class Proyecto(models.Model):  # ← "Model" con M mayúscula
    titulo = models.CharField(max_length=200)  # ← "CharField" con C mayúscula
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    tecnologias = models.CharField(max_length=300)
    url_demo = models.URLField(blank=True, null=True)
    url_repositorio = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_creacion']
