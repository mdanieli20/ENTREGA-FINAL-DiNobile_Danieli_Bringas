from django.urls import path
from .views import home, crear_noticia, nosotros
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('crear-noticia/', crear_noticia, name='crear_noticia'),
    path('noticias/', views.ListadoNoticias.as_view(), name='listado_noticias'),
    path('mostrar-noticia/<int:pk>/', views.MostrarNoticia.as_view(), name='mostrar_noticia'),
    path('editar-noticias/<int:pk>/', views.EditarNoticia.as_view(), name='editar_noticia'),
    path('eliminar-noticia/<int:pk>/', views.EliminarNoticia.as_view(), name='eliminar_noticia'),
    path('nosotros/', nosotros, name='nosotros')
]