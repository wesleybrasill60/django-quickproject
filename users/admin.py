from django.contrib import admin
from users.models import (
    Login, Reserva, Lista, Historico, Cadastro, Usuario)

# Register your models here.
admin.site.register(Cadastro)
admin.site.register(Login)
admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(Lista)
admin.site.register(Historico)
