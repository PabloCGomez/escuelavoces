from django import forms
# from tinymce.widgets import TinyMCE
from .models import Noticia


        
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "contenido", "estado"]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "contenido": forms.Textarea(attrs={
                "class": "form-control summernote"  # 👈 clave
            }),
            "estado": forms.Select(attrs={
                "class": "form-select"
            }),
        }
        
from django import forms
from .models import MensajePopUp

class MensajePopUpForm(forms.ModelForm):
    class Meta:
        model = MensajePopUp
        fields = [
            "titulo",
            "mensaje",
            "imagen",
            "link",
            "tipo",
            "activo",
            "fecha_inicio",
            "fecha_fin",
        ]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "fecha_inicio": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "fecha_fin": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }
        
                
        
