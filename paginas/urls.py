from django.urls import path
from .views import IndexView, SobreView, SalgadosView, TesteView

urlpatterns = [
    #path ('endereço/', MinhaView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('sobre', SobreView.as_view(), name='sobre'),
    path('salgados', SalgadosView.as_view(), name='salgados'),
    path('teste', TesteView.as_view(), name='teste'),
    
]