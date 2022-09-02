from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = RichTextField(null=True)
    fecha_creacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)
    def __str__(self):
        return f'Titulo de la noticia {self.titulo}'