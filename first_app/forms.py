from django import forms
from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = ['tipo_investimento', 'valor', 'descricao'] #ou '__all__' para todos os campos
        labels = {
            'tipo_investimento': 'Tipo de Investimento',
            'valor': 'Valor',
            'descricao': 'Descrição',
        } 