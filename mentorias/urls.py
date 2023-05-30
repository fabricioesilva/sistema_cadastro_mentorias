from django.urls import path

from .views import (
    MentoriasView, criar_mentoria, mentoria_detalhe, alunos_mentor,
    simulados_mentor, arquivos_mentor, materias_mentor,
    cadastrar_aluno, cadastrar_simulado, enviar_arquivo,
    cadastrar_materia, aluno_detalhe, editar_aluno, aluno_matricular,
    mentoria_apagar, simulado_detalhe, materia_detalhe, cadastrar_gabarito
)


app_name = 'mentorias'

urlpatterns = [
    path('', MentoriasView.as_view(), name='mentorias_home'),
    path('criar/', criar_mentoria, name='criar_mentoria'),
    path('<int:pk>/', mentoria_detalhe, name='mentoria_detalhe'),
    path('alunos/<int:pk>/', aluno_detalhe, name="aluno_detalhe"),
    path('alunos/editar/<int:pk>/', editar_aluno, name="editar_aluno"),
    path('alunos/', alunos_mentor, name='alunos'),
    path('matricular/<int:pk>/', aluno_matricular, name="aluno_matricular"),
    path('apagar/<int:pk>/', mentoria_apagar, name='mentoria_apagar'),
    path('simulados/', simulados_mentor, name='simulados'),
    path('arquivos/', arquivos_mentor, name='arquivos'),
    path('materias/', materias_mentor, name='materias'),
    path('materias/<int:pk>/', materia_detalhe, name="materia_detalhe"),
    path('alunos/cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('simulados/cadastrar/', cadastrar_simulado, name='cadastrar_simulado'),
    path('simulados/<int:pk>/', simulado_detalhe, name="simulado_detalhe"),
    path('simulados/<int:pk>/gabarito/cadastrar/', cadastrar_gabarito, name="cadastrar_gabarito"),
    path('arquivos/enviar/', enviar_arquivo, name='enviar_arquivo'),
    path('materias/cadastrar/', cadastrar_materia, name='cadastrar_materia'),

    # path('gabaritos/cadastrar/', cadastrar_gabarito, name='cadastrar_gabarito'),
    # path('gabaritos/', gabaritos_mentor, name='gabaritos'),
]
