from cProfile import label
from django import forms

class Cadastro(forms.Form):
    nome = forms.CharField(label='nome', required=True)
    email = forms.EmailField(label='email', required=True)
    senha = forms.CharField(label='senha', required=True)