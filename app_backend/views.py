from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Autor_Serializer, Comuna_Serializer, Direccion_Serializer, Biblioteca_Serializer, Libro_Serializer, TipoCategoria_Serializer, Categoria_Serializer, Lector_Serializer, Prestamo_Serializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo

# Create your views here.


def pagina_inicio(request):
    return render(request, 'app_backend/index.html')


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