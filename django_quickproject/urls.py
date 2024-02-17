from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.api.views import (
    CadastroViewSet, LoginViewSet, ReservaViewSet,
    ListaViewSet, HistoricoViewSet, UsuarioViewSet
)

router = SimpleRouter()

urlpatterns = [
    # Admin URL
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path("cadastro/", CadastroViewSet.as_view(
        {'get': 'list'}), name="cadastro"),
    path("login/", LoginViewSet.as_view(
        {'get': 'list'}), name="login"),
    path("usuario/", UsuarioViewSet.as_view(
        {'get': 'list'}), name="usuario"),
    path("reserva/", ReservaViewSet.as_view(
        {'get': 'list'}), name="reserva-list"),
    path("lista/", ListaViewSet.as_view(
        {'get': 'list'}), name="lista-list"),
    path("historico/", HistoricoViewSet.as_view(
        {'get': 'list'}), name="historico-list"),
        ]
