from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Autor_Serializer, Comuna_Serializer, Direccion_Serializer, Biblioteca_Serializer, Libro_Serializer, TipoCategoria_Serializer, Categoria_Serializer, Lector_Serializer, Prestamo_Serializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login/')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def pagina_inicio(request):
    MENSAJE_BIENVENIDA = "¡Bienvenido a la Biblioteca!" # Constante para el mensaje de bienvenida

    request.session[MENSAJE_BIENVENIDA] = "¡Bienvenido a la Biblioteca!"

    mensaje_bienvenida = request.session.get(MENSAJE_BIENVENIDA)

    if 'mensaje_bienvenida' in request.session:
        del request.session[MENSAJE_BIENVENIDA]
    return render(request, 'app_backend/index.html', {'mensaje_bienvenida': mensaje_bienvenida})

class nacionalidad_viewset(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer


class autor_viewset(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer


class comuna_viewset(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer


class direccion_viewset(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer


class biblioteca_viewset(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = Biblioteca_Serializer


class lector_viewset(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer


class tipo_categoria_viewset(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoria_Serializer


class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = Categoria_Serializer


class libro_viewset(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer


class prestamo_viewset(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer