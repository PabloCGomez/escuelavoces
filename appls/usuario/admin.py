from django.contrib import admin

# Register your models here.
fieldsets = (
    (None, {"fields": ("email", "password")}),
    ("Información personal", {"fields": ("first_name", "last_name")}),
    ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser",
                             "is_content_supervisor",  # 👈 agregar
                             "groups", "user_permissions")}),
    ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
)
