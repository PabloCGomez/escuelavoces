from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "tu email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "tu contraseña"
    }))


from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
