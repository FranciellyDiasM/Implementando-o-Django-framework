from django.urls import path
from . import views

urlpatterns = [
    # Rotas padrão (sem extensão .html)
    path('', views.index, name='index'),
    path('brasil/', views.brasil, name='brasil'),
    path('movimento/', views.movimento, name='movimento'),
    path('origem/', views.origem, name='origem'),
    path('prevencao/', views.prevencao, name='prevencao'),
    
    # Rotas com extensão .html
    path('index.html', views.index, name='index_html'),
    path('brasil.html', views.brasil, name='brasil_html'),
    path('movimento.html', views.movimento, name='movimento_html'),
    path('origem.html', views.origem, name='origem_html'),
    path('prevencao.html', views.prevencao, name='prevencao_html'),
]
