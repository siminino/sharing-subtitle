from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from projetos.models import Projeto


def pagina_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    return TemplateResponse(request, 'projetos/projeto.html', {'projeto': projeto})

def listagem_projetos(request):
    projetos = Projeto.objects.all().order_by('titulo')
    return TemplateResponse(request, 'projetos/listagem_projetos.html', {'projetos': projetos})

def view_test(request):
    return TemplateResponse(request, 'base.html')

