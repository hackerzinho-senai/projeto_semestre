from django import forms
from .models import Produto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'ativo']
        labels = {
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição',
            'ativo': 'Ativo',
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'valor', 'descricao', 'quantidade', 'imagem', 'ativo']
        labels = {
            'nome': 'Nome do Produto',
            'categoria': 'Categoria',
            'valor': 'Valor',
            'descricao': 'Descrição',
            'quantidade': 'Quantidade',
            'imagem': 'Imagem',
            'ativo': 'Ativo',
        }
