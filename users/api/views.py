from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import (
     CadastroSerializer, HistoricoSerializer, ListaSerializer, LoginSerializer,
     UsuarioSerializer, ReservaSerializer)

from users.models import (
    Cadastro, Login, Usuario, Historico, Lista, Reserva)


class CadastroViewSet(ModelViewSet):
    serializer_class = CadastroSerializer
    permission_classes = [AllowAny]
    queryset = Cadastro.objects.all()
    http_method_names = ['get', 'put']


class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = Login.objects.all()
    http_method_names = ['get', 'put']


class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'put']


class ReservaViewSet(ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [AllowAny]
    queryset = Reserva.objects.all()
    http_method_names = ['get', 'put']


class ListaViewSet(ModelViewSet):
    serializer_class = ListaSerializer
    permission_classes = [AllowAny]
    queryset = Lista.objects.all()
    http_method_names = ['get', 'put']


class HistoricoViewSet(ModelViewSet):
    serializer_class = HistoricoSerializer
    permission_classes = [AllowAny]
    queryset = Historico.objects.all()
    http_method_names = ['get', 'put']
