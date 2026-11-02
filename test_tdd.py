import pytest
from calculadora_tdd import CalculadoraDescontoTDD

calc = CalculadoraDescontoTDD()

def test_desconto_10_acima_de_500():
    assert calc.calcular(600) == 540

def test_desconto_20_acima_de_1000():
    assert calc.calcular(1500) == 1200

def test_vip_ganha_5_a_mais():
    assert calc.calcular(1500, vip=True) == 1140

def test_frete_abaixo_de_100():
    assert calc.calcular(80) == 95