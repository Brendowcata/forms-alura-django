from django.http import request
from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms

def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    dados = {
        'form':form,
        'pessoa_form':pessoa_form
    }
    return render(request, 'index.html', dados)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            dados = {
                'form':form,
                'pessoa_form':pessoa_form
            }
            return render(request, 'minha_consulta.html', dados)
        else:
            print('Form inválido')
            dados = {
                'form':form,
                'pessoa_form':pessoa_form
            }
            return render(request, 'index.html', dados)
