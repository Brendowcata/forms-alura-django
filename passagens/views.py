from django.http import request
from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    dados = {
        'form':form
    }
    return render(request, 'index.html', dados)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            dados = {
            'form':form
            }
            return render(request, 'minha_consulta.html', dados)
        else:
            print('Form inválido')
            dados = {
             'form':form
            }
            return render(request, 'index.html', dados)
