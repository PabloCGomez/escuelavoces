from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def supervisor_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user.is_content_supervisor:
            return redirect("home")  # o página 403
        return view_func(request, *args, **kwargs)
    return wrapper
