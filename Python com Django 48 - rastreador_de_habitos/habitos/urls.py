from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_habito, name='criar_habito'),
    path('listar/', views.listar_habitos, name='listar_habitos'),
    path('registrar/<int:habito_id>/', views.registrar_habito, name='registrar_habito'),
    path('relatorio/<int:habito_id>/', views.relatorio_habito, name='relatorio_habito'),
    path('editar/<int:habito_id>/', views.editar_habito, name='editar_habito'),
    path('excluir/<int:habito_id>/', views.excluir_habito, name='excluir_habito'),
    path("habitos/editar_registro/<int:registro_id>/", views.editar_registro, name="editar_registro"),
    path("habitos/excluir_registro/<int:registro_id>/", views.excluir_registro, name="excluir_registro"),
]
