from django.urls import path, include
from rest_framework import routers
from app_backend import views

router = routers.DefaultRouter()

router.register(r'nacionalidades', views.nacionalidad_viewset)
router.register(r'autores', views.autor_viewset)
router.register(r'comunas', views.comuna_viewset)
router.register(r'direcciones', views.direccion_viewset)
router.register(r'bibliotecas', views.biblioteca_viewset)
router.register(r'lectores', views.lector_viewset)
router.register(r'tipos_categorias', views.tipo_categoria_viewset)
router.register(r'categorias', views.categoria_viewset)
router.register(r'libros', views.libro_viewset)
router.register(r'prestamos', views.prestamo_viewset)

urlpatterns = [
    path('', include(router.urls))
]