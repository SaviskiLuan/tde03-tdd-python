import pytest
from calculadora_tdd import CalculadoraDescontoTDD

calc = CalculadoraDescontoTDD()

def test_desconto_10_acima_de_500():
    assert calc.calcular(600) == 540