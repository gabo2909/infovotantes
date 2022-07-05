from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *
from .viewset import *

router = routers.SimpleRouter()
router.register(r'api/infovotantes/departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'api/infovotantes/municipios', MunicipioViewSet, basename='municipios')
router.register(r'api/infovotantes/comunas', ComunaViewSet, basename='comunas')
router.register(r'api/infovotantes/barrios', BarrioViewSet, basename='barrios')
router.register(r'api/infovotantes/puesto-votacion', PuestoVotacionViewSet, basename='puesto_votacion')
router.register(r'api/infovotantes/votantes', VotanteViewSet, basename='votantes')

urlpatterns = [
    path('registrar-usuario', RegistrarUsuarioView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()), 
    path('user', UserView.as_view()),
]