from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import supervisor_required
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy


@login_required(login_url="/usuario/login/")
def inicio(request):
    return redirect("dashboard") 
#    return render(request, "sitio/index.html")

class CustomLoginView(LoginView):
    template_name = "usuario/login.html"

    def get_success_url(self):
        return reverse_lazy("dashboard")
    


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático
            return redirect("/sitio/")  # Redirigir al home o dashboard
    else:
        form = RegistroForm()

    return render(request, "usuario/registro.html", {"form": form})



#@supervisor_required
def dashboard(request):
    
    return render(request, "usuario/dashboard.html")