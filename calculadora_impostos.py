class Imposto(object):
    def __init__(self, aliquota):
        self._aliquota = aliquota
    
    def calcular(self,produto):
        return produto.valor * self._aliquota

class ImpostoIPI(Imposto):
    def __init__ (self):
        Imposto.__init__(self, 0.3)

class ImpostoICMS(Imposto):
    def __init__(self):
        Imposto.__init__(self, 0.25)

class ImpostoISS(Imposto):
    def __init__(self):
        Imposto.__init__(self, 0.17) 

'''
''produto_fabricado --> IPI (30%) , ICMS (15%)
''produto_revendido --> ICMS (25%)
''serviço           --> ISS (17%)
'''

class CalculadoraImposto():
    raise Exception("Nao foi implementada a estrategia!")

class CalculaImpostoProdutoFabricadoStrategy(CalculadoraImposto):
    def calcula_impostos(self, produto):
        #produto_fabricado --> IPI (30%) , ICMS (25%)
        _vl_total = ImpostoIPI().calcular(produto)
        _vl_total = ImpostoICMS().calcular(produto)
        return _vl_total

class CalculaImpostoProdutoRevendidoStrategy(CalculadoraImposto):
    def calcula_impostos(self,produto):
        #produto_revendido --> ICMS (25%)
        return ImpostoICMS().calcular(produto)

class CalculaImpostoServicoStrategy(CalculadoraImposto):
    def calcula_impostos(self, produto):
        #serviço           --> ISS (17%)
        return ImpostoISS().calcular(produto)
