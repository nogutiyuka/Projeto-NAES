from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    #path ('endereço/', MinhaView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('sobre', SobreView.as_view(), name='sobre'),
    
]