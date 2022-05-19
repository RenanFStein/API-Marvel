from django.contrib import admin
from .models import *

# Register your models here.

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email')
    list_per_page = 20
admin.site.register(Usuario, Usuarios)