from django.urls import path
from . import views

urlpatterns = [
    path("popup/nuevo/", views.popup_crear, name="popup_crear"),
    path("popup/<uuid:id>/editar/", views.popup_editar, name="popup_editar"),
    path("popup/<uuid:id>/eliminar/", views.popup_eliminar, name="popup_eliminar"),   
    path("popup/listar/", views.popup_listar, name="popup_listar"),
    path("popup/foto/<int:id>/eliminar/", views.popup_foto_eliminar,  name="popup_foto_eliminar"),
    
    path("noticias_lista/", views.noticias_lista, name="noticias_lista"),   
    path("crear/",  views.crear_noticia,   name="crear_noticia"),
    path("noticias/", views.noticias_lista_public, name="noticias_lista_public"),   
    path("noticias/<uuid:id>/editar/",   views.editar_noticia,  name="editar_noticia"),
    path("noticias/<uuid:id>/detalle/",  views.detalle_noticia, name="detalle_noticiae"),
    path('noticias/<uuid:id>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
    path('foto/<uuid:id>/eliminar/', views.noticia_foto_delete,  name='noticia_foto_delete'),        
]
