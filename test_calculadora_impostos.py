from calculadora_impostos import CalculaImpostoProdutoFabricadoStrategy, CalculaImpostoProdutoRevendidoStrategy,CalculaImpostoServicoStrategy
from ecommerce import Produto

def test_ipi():
    fabr = Produto ('Bicicleta', 500, CalculaImpostoProdutoFabricadoStrategy())
    assert fabr.calImpostoStrategy.calcula_impostos(fabr) == 150

def test_icms():
    fabr = Produto ('Lanterna', 50, CalculaImpostoProdutoRevendidoStrategy())
    assert fabr.calImpostoStrategy.calcula_impostos(fabr) == 12.5

def test_iss():
    fabr= Produto ('Manutencao', 150, CalculaImpostoServicoStrategy())
    assert fabr.calImpostoStrategy.calcula_impostos(fabr) == 25.5