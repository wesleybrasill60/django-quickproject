from rest_framework import serializers
from users.models import Cadastro, Historico, Login, Reserva, Lista, Usuario


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'nome', 'email', 'senha', 'confSenha', 'fcmToken']
        read_only_fields = ['id', 'fcmToken']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['email', 'senha']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'fcmToken']

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['data', 'mesas', 'hora', 'nome']
        read_only_fields = ['nome']


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['data', 'mesas', 'hora', 'nome']
        read_only_fields = ['nome']


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ['data', 'mesas', 'hora', 'nome']
        read_only_fields = ['nome']
