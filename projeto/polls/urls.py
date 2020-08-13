from django.urls import path
from . import views

# Neste tutorial temos um app apenas.  Mas em um projeto podemos ter vários apps com seus urls.py
# Imaginemos que tempos dois apps.  Um polls e outro products... Por exemplo
# Se ambos tiverem url com name='detail'
# Como o Django vai saber a que app você está se referindo?  
# para isso vamos colocar o app_name
# quando usarmos o {% url 'detail' %} passaremos a usar {% url 'polls:detail' %}

app_name = 'polls'

urlpatterns = [
    # Exemplo: /polls/
    path('', views.index, name='index'),
    # Exemplo: /polls/1/
    path('<int:question_id>', views.detail, name='detail'),
    # Exemplo: /polls/1/results
    path('<int:question_id>/results/', views.results, name='results'),
    # Exemplo: /polls/1/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
