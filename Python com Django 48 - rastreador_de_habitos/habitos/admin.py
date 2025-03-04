from django.contrib import admin
from .models import Habito, Registro

class RegistroInline(admin.TabularInline):
    model = Registro
    extra = 1  # Número de registros em branco para adicionar diretamente no formulário de hábito

class HabitoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicial', 'data_final')  # Exibir essas colunas na lista de hábitos
    search_fields = ('nome', 'descricao')  # Permitir buscar por nome ou descrição
    inlines = [RegistroInline]  # Permitir adicionar registros diretamente dentro do formulário do hábito

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('habito', 'data', 'cumprido')  # Exibir hábito, data e se foi cumprido ou não
    list_filter = ('cumprido', 'habito')  # Filtrar por cumprimento ou hábito
    search_fields = ('habito__nome',)  # Permitir buscar registros por nome do hábito

# Registrar os modelos com a administração
admin.site.register(Habito, HabitoAdmin)
admin.site.register(Registro, RegistroAdmin)
