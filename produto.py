class Produto:
    def __init__(self, codigo, nome, quantidade, valor_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def __str__(self):
        return f'Codigo: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nValor_unitario: {self.valor_unitario}\n'
