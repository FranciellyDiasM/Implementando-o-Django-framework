http://127.0.0.1:8000/

## Implementação de um site utilizando o framework Django, adaptando um design já existente.

 1. **Instalar Django e configurar o projeto**
- Certifique-se de ter o Python instalado.
- Instale o Django:
```
bash

pip install django
```
Crie um novo projeto Django:
```
bash

django-admin startproject meu_projeto
cd meu_projeto
```
Execute o servidor para confirmar que tudo está funcionando:
```
bash

python manage.py runserver
```
Acesse `http://127.0.0.1:8000` para verificar.

2.**Criar um aplicativo no Django**
   Crie um aplicativo para seu site:
```
bash

python manage.py startapp meu_site
```
Adicione o aplicativo ao arquivo settings.py do projeto:
```
python

INSTALLED_APPS = [
    ...
    'meu_site',
]
```
3. **Configurar as URLs**
No arquivo meu_projeto/urls.py, inclua o aplicativo nas rotas:
```
python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meu_site.urls')),  # Inclui as URLs do app
]
```
No aplicativo, crie um arquivo urls.py em meu_site e adicione:
```
python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
]
```
4. **Criar a view**
No arquivo meu_site/views.py, defina a view:
```
python

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Renderiza o template HTML
```

5. Organizar os arquivos HTML e CSS
- Crie uma pasta chamada templates dentro do aplicativo meu_site.

- Copie seus arquivos HTML para meu_site/templates.

- Para o CSS, crie uma pasta static dentro de meu_site, assim:
  ```
  repositório
  
  meu_site/
    static/
        css/
            estilo.css 
           
E coloque seus arquivos CSS lá.

6. **Conectar os arquivos estáticos**
No HTML, ajuste as referências ao CSS para usar a tag {% static %} do Django.
```
html

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static 'css/estilo.css' %}">
    <title>Meu Site</title>
</head>
<body>
    <h1>Bem-vindo ao meu site!</h1>
</body>
</html>
```
Certifique-se de ativar os arquivos estáticos no settings.py:
```
python

STATIC_URL = '/static/'
```
7. **Executar o projeto**
Execute o servidor novamente:
```
bash

python manage.py runserver
```
Acesse `http://127.0.0.1:8000` e veja seu site funcionando com Django!
