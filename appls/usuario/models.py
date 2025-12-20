
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    # Campos básicos
    
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    is_content_supervisor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_ultimo_ingreso=models.DateTimeField(default=timezone.now)

    # Roles posibles
    ADMINISTRADOR = "administrador"
    PROFESOR  = "profesor"
    DIRECTOR  = "director"
    APODERADO = "apoderado"
    ALUMNO    = "alumno"
    SUPER_ADMINSTRADOR ="Adm Plataforma"

    ROLE_CHOICES = [
        (ADMINISTRADOR, "Administrador de Colegio"),
        (PROFESOR, "Profesor"),
        (DIRECTOR, "Director"),
        (APODERADO, "Apoderado"),
        (ALUMNO, "Alumno"),
        (SUPER_ADMINSTRADOR, "Administrador e-Colegio")
    ]

    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default=APODERADO)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"