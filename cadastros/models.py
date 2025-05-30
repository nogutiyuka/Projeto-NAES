from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def total_venda(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidades"

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.ForeignKey('Genero', on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

    def em_estoque(self):
        return self.estoque > 0

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.cliente}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

