from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def login_view(request):
    return render(
        request,
        'login.html'
    )

def register_view(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                )
                user.save()
                messages.success(request, 'El usuario se registro correctamente, ahora inicie sesion!')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'El usuario ya se encuentra registrado!')
                return __render_register_view(request)
        else:
            messages.error(request, 'Las contrasenas no coinciden!')
            return __render_register_view(request)
    else:
        return __render_register_view(request)
    
def __render_register_view(request):
    return render(
        request,
        'register.html',
        {
            'form': UserCreationForm()
        }
    )