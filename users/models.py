import uuid
from django.db import models


class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50)
    confSenha = models.CharField(max_length=50)
    fcmToken = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cadastro"
        verbose_name_plural = "Cadastros"


class Login(models.Model):
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Login"
        verbose_name_plural = "Logins"


class Usuario(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Reserva(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    data = models.DateField(blank=False, null=False)
    mesas = models.IntegerField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


class Historico(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField(blank=False, null=False)
    mesas = models.IntegerField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.data}, {self.mesas}, {self.hora}, {self.nome}"

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"


class Lista(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField(blank=False, null=False)
    mesas = models.IntegerField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.data}, {self.mesas}, {self.hora}, {self.nome}"

    class Meta:
        verbose_name = "Lista"
        verbose_name_plural = "Listas"
