class contaBancaria:
    def __init__(self,titular,tipo, saldo):
        self.titular = titular
        self.tipo = tipo
        self.__saldo = saldo

    def exibirSaldo (self):
        print(f'O saldo da conta é {self.__saldo}')


contaSamuel = contaBancaria('Samuel', 'Poupança', 100)

print(f'{contaSamuel.tipo}, {contaSamuel.titular}')

contaSamuel.exibirSaldo()