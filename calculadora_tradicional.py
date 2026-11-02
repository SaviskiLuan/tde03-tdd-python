class CalculadoraDescontoTradicional:
    def calcular(self, valor, vip=False):
        if valor <= 0:
            raise ValueError("Valor do pedido deve ser maior que zero")
        if valor > 1000:
            valor = valor * 0.80
        elif valor > 500:
            valor = valor * 0.90
        if vip:
            valor = valor * 0.95
        if valor < 100:
            valor = valor + 15
        return round(valor, 2)