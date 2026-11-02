class CalculadoraDescontoTDD:
    def calcular(self, valor, vip=False):
        if valor <= 0:
            raise ValueError("Valor do pedido deve ser maior que zero")
        valor = self._desconto_por_faixa(valor)
        if vip:
            valor = valor * 0.95
        if valor < 100:
            valor = valor + 15
        return round(valor, 2)

    def _desconto_por_faixa(self, valor):
        if valor > 1000:
            return valor * 0.80
        if valor > 500:
            return valor * 0.90
        return valor