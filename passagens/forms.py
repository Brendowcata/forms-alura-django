from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida':'Data de ida', 'data_volta':'Data de volta', 'informacoes':'Informações', 'data_pesquisa':'Data da pesquisa', 'classe_viagem':'Classe do vôo'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker(),
        }
    
    
    def clean(self):
        destino = self.cleaned_data.get('destino')
        origem = self.cleaned_data.get('origem')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        
        lista_error = {}
        campo_tem_numero(origem, 'origem', lista_error)
        campo_tem_numero(destino, 'destino', lista_error)
        origem_destino_iguais(origem, destino, lista_error)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_error)
        data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_error)
        if lista_error is not None:
            for erro in lista_error:
                mensagem_erro = lista_error[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
