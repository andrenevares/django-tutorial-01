from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import HttpResponse
from django.http import Http404


def index(request):
    lista_das_ultimas_questoes = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([questao.question_text for questao in lista_das_ultimas_questoes])
    context = {
        'lista_das_ultimas_questoes': lista_das_ultimas_questoes,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except:
        raise Http404(f"A questão nº {question_id} aparentemente não existe")

    return render (request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão de nº %s." % question_id)