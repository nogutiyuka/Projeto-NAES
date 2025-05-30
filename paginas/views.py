from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class SalgadosView(TemplateView):
    template_name = 'paginas/salgados.html'

class TesteView(TemplateView):
    fields = ['nome', 'preco', 'categoria', 'descricao', 'imagem']
    success_url = '/paginas/teste/'
    template_name = 'paginas/adicionarItemModelo.html'