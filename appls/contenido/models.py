from django.db import models
import uuid


class MensajePopUp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TIPO_CHOICES = (
        ("info", "Información"),
        ("alerta", "Alerta"),
        ("promo", "Promoción"),
    )

    titulo = models.CharField(max_length=150)
    mensaje = models.TextField(blank=True,null=True)
    imagen = models.ImageField(upload_to="popups/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="info")

    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

    @property
    def esta_visible(self):
        """Devuelve True si el popup debe mostrarse hoy."""
        from django.utils import timezone
        ahora = timezone.now()

        if not self.activo:
            return False

        if self.fecha_inicio and ahora < self.fecha_inicio:
            return False

        if self.fecha_fin and ahora > self.fecha_fin:
            return False

        return True

class MensajePopUpFoto(models.Model):
    mesajePU = models.ForeignKey(MensajePopUp, on_delete=models.CASCADE, related_name="fotosPopUP")
    imagen = models.ImageField(upload_to="imagenes/")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.mensajePU.titulo}"


class Noticia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ESTADOS = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    contenido = models.TextField(blank=True)  # 👈 recomendado
    estado = models.CharField(max_length=10, choices=ESTADOS, default='borrador')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo

class NoticiaFoto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="fotos")
    imagen = models.ImageField(upload_to="imagenes/")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.noticia.titulo}"



from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Imagen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Datos Base
    imagen = models.ImageField(upload_to="imagenes/")
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    # Relación Genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Orden
    orden = models.PositiveIntegerField(default=0)

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', '-creado']

    def __str__(self):
        return f"Imagen {self.titulo or self.id}"
