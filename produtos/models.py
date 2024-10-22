from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = False, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome
