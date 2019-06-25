class Conta:
    __init__(self, titular, numero, saldo, limite):
        print("Inicializando uma conta")
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
