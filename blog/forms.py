from unittest.util import _MAX_LENGTH
from django import forms
from ckeditor.widgets import CKEditorWidget

class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(widget=CKEditorWidget())
    fecha_creacion = forms.DateField(required=False)
    imagen = forms.ImageField(required=False)
    
class BusquedaNoticia(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)