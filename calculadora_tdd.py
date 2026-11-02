class CalculadoraDescontoTDD:
    def calcular(self, valor, vip=False):
        valor = self._desconto_por_faixa(valor)
        if vip:
            valor = valor * 0.95
        return round(valor, 2)

    def _desconto_por_faixa(self, valor):
        if valor > 1000:
            return valor * 0.80
        if valor > 500:
            return valor * 0.90
        return valor