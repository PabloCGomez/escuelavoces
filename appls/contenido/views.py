from django.shortcuts import render, get_object_or_404
from .models import Noticia , MensajePopUpFoto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import MensajePopUp
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Noticia, NoticiaFoto
from .forms import NoticiaForm




@login_required
def noticias_lista(request):
    noticia = Noticia.objects.all()
    return render(request, "contenido/lista_noticias.html", {"noticia": noticia})


def noticias_lista_public(request):
    noticias = Noticia.objects.filter(
        estado="publicado"
    ).order_by("-fecha_publicacion")

    return render(request, "noticias_blog.html", {
        "noticia": noticias
    })




@login_required
def crear_noticia(request):   
    noticia = Noticia.objects.create(
        titulo="",
        contenido="",
        estado="borrador"
    )
    return redirect("editar_noticia", id=noticia.id)


@login_required
def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, "contenido/editar_noticia.html", {"noticia": noticia})



@login_required
def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            # Guardamos la noticia
            noticia = form.save(commit=False)
            #  noticia.estado = "publicado"  # O déjalo form.cleaned_data["estado"]
            noticia.save()

            # Guardar imágenes múltiples (input name="imagenes")
            imagenes = request.FILES.getlist("imagenes")
            for img in imagenes:
                NoticiaFoto.objects.create(
                    noticia=noticia,
                    imagen=img
                )
        # Si no es válido, devolvemos los errores para mostrarlos en el frontend
        else:
            for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"Error en {field}: {error}")
                        

            return redirect("noticias_lista")
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, "contenido/crear.html", {"form": form,"noticia": noticia})



from django.shortcuts import get_object_or_404, redirect
from .models import NoticiaFoto

def noticia_foto_delete(request, id):
    foto = get_object_or_404(NoticiaFoto, id=id)
    noticia_id = foto.noticia.id

    # Eliminar archivo físico (opcional pero recomendado)
    if foto.imagen:
        foto.imagen.delete(save=False)

    # Eliminar registro BD
    foto.delete()

    return redirect("editar_noticia", id=noticia_id)
    
    
    
@login_required
def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    # Eliminar imágenes físicas asociadas
    for foto in noticia.fotos.all():
        if foto.imagen:
            foto.imagen.delete(save=False)
        foto.delete()

    # Eliminar la noticia
    noticia.delete()

    return redirect("noticias_lista")






def popup_activo(request):
    ahora = timezone.now()

    popup = (
        MensajePopUp.objects
        .filter(activo=True)
        .filter(
            Q(fecha_inicio__lte=ahora) | Q(fecha_inicio__isnull=True),
            Q(fecha_fin__gte=ahora) | Q(fecha_fin__isnull=True),
        )
        .order_by("-creado")
        .first()
    )

    return {"popup_activo": popup}





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MensajePopUp
from .forms import MensajePopUpForm

@login_required
def popup_crear(request):
    if request.method == "POST":
        form = MensajePopUpForm(request.POST, request.FILES)

        if form.is_valid():
            popup = form.save()

            # 🔹 GUARDAR IMÁGENES
            imagenes = request.FILES.getlist("imagenes")
            for img in imagenes:
                MensajePopUpFoto.objects.create(
                    mesajePU=popup,
                    imagen=img
                )
            return redirect("popup_editar", id=popup.id)
        # Si no es válido, devolvemos los errores para mostrarlos en el frontend
        else:
            for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"Error en {field}: {error}")

    else:
        form = MensajePopUpForm()

    return render(request, "contenido/crear_popup.html", {
        "form": form,
        "titulo": "Crear mensaje PopUp"
    })



from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MensajePopUp, MensajePopUpFoto
from .forms import MensajePopUpForm

@login_required
def popup_editar(request, id):
    popup = get_object_or_404(MensajePopUp, id=id)

    if request.method == "POST":
        form = MensajePopUpForm(request.POST, request.FILES, instance=popup)

        if form.is_valid():
            popup = form.save()

            # 🔹 NUEVAS IMÁGENES
            imagenes = request.FILES.getlist("imagenes")
            for img in imagenes:
                MensajePopUpFoto.objects.create(
                    mesajePU=popup,
                    imagen=img
                )

            messages.success(request, "Popup actualizado correctamente")
            return redirect("popup_editar", id=popup.id)
    else:
        form = MensajePopUpForm(instance=popup)

    return render(request, "contenido/crear_popup.html", {
        "form": form,
        "popup": popup,
        "titulo": "Editar mensaje PopUp"
    })



@login_required
def popup_listar(request):
    Mensaje = MensajePopUp.objects.all()
    return render(request, "contenido/lista_mensajepopup.html", {"mensaje": Mensaje})


@login_required
def popup_eliminar(request, id):
    popup = get_object_or_404(MensajePopUp, id=id)

    
    for foto in popup.fotosPopUP.all():
            foto.imagen.delete(save=False)
    popup.delete()

    messages.success(request, "Popup eliminado correctamente")
    return redirect("popup_listar")


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MensajePopUpFoto


@login_required
def popup_foto_eliminar(request, id):
    foto = get_object_or_404(MensajePopUpFoto, id=id)

    popup_id = foto.mesajePU.id  # para volver al editor

    # 🔥 eliminar archivo físico
    foto.imagen.delete(save=False)

    # 🔥 eliminar registro
    foto.delete()

    messages.success(request, "Imagen eliminada correctamente")
    return redirect("popup_editar", id=popup_id)
