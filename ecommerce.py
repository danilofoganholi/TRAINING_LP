from calculadora_impostos import CalculaImpostoProdutoFabricadoStrategy, CalculaImpostoProdutoRevendidoStrategy, CalculaImpostoServicoStrategy

class Produto(object):
    def __init__ (self,nome,valor, calImpostoStrategy):
        self.nome = nome
        self.valor = valor
        # produto_fabricado, produto_revendido , serviço 
        self.calImpostoStrategy = calImpostoStrategy

    def calculadora_impostos(self):
        return self.calImpostoStrategy.calculadora_impostos(self)

class Venda (object):
    def __init__(self, produtos):
        self.produtos = produtos


'''
produtos = {
    1 : Produto ('Bicicleta', 500, CalculaImpostoProdutoFabricadoStrategy()),
    2 : Produto ('Lanterna', 50, CalculaImpostoProdutoRevendidoStrategy()),
    3 : Produto ('Manutencao', 150, CalculaImpostoServicoStrategy())
}
'''