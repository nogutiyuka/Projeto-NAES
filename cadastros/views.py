from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'cargo', 'salario']
    template_name = 'cadastros/funcionario_form.html'
    success_url = '/cadastros/funcionario/listar/'