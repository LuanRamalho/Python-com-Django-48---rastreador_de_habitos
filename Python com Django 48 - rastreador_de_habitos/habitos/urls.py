from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_habito, name='criar_habito'),
    path('listar/', views.listar_habitos, name='listar_habitos'),
    path('registrar/<int:habito_id>/', views.registrar_habito, name='registrar_habito'),
    path('relatorio/<int:habito_id>/', views.relatorio_habito, name='relatorio_habito'),
]
