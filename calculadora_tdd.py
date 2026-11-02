class CalculadoraDescontoTDD:
        def calcular(self, valor, vip=False):
            if valor > 1000:
                return valor * 0.80
            if valor > 500:
                return valor * 0.90
            return valor