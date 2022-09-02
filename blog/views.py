from django.shortcuts import render, redirect
from .forms import FormNoticia, BusquedaNoticia
from .models import Noticia
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Noticia


def home(request):
    return render(request, 'home.html')


def crear_noticia(request):    
    if request.method == 'POST':
        form = FormNoticia(request.POST,request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            noticia = Noticia(
                titulo=data.get('titulo'),
                contenido=data.get('contenido'),
                fecha_creacion=fecha,
                imagen=data.get('imagen')
            )
            noticia.save()

            return redirect('listado_noticias')
        
        else:
            return render(request, 'crear_noticia.html', {'form': form})
            
    
    form_noticia = FormNoticia()
    
    return render(request, 'crear_noticia.html', {'form': form_noticia})

class ListadoNoticias(ListView):
    model=Noticia
    template_name = 'listado_noticias.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaNoticia()
        return context
    
def nosotros(request):
    return render(request, 'nosotros.html')

class EditarNoticia(LoginRequiredMixin, UpdateView):
    model=Noticia
    template_name = 'editar_noticia.html'
    success_url = '/noticias'
    fields = ['titulo', 'contenido', 'fecha_creacion','imagen']


class EliminarNoticia(LoginRequiredMixin, DeleteView):
    model=Noticia
    template_name = 'eliminar_noticia.html'
    success_url = '/noticias'
    
class MostrarNoticia(DetailView):
    model = Noticia
    template_name = 'mostrar_noticia.html'