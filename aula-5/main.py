class ContaBancaria:
    def __init__(self, titular,tipo, agencia, conta, saldo):
        self.titular = titular
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    def ExibirDadosDaConta(self):
        print(f'Titular..: {self.titular}')
        print(f'Tipo de conta..: {self.tipo}')
        print(f'Agencia Bancária..: {self.agencia}')
        print(f'Numero da conta..: {self.conta}')
        print(f'Saldo Total da conta..: {self.saldo}')

    def SaqueBancario(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente')
        else:
            self.saldo -= valor

    def DepositoBancario(self, valor):
        self.saldo += valor


contaSamuel = ContaBancaria('Samuel',"Conta Corrente","0001",40607, 4500)
contaDaniel = ContaBancaria('Daniel',"Conta Poupança","0002",11155, 5000)
contaElias = ContaBancaria('Elias',"Conta Salario","0003",11445, 1000)

contaSamuel.ExibirDadosDaConta()
contaDaniel.ExibirDadosDaConta()
contaElias.ExibirDadosDaConta()




valorSaque = float(input("Digite o valor de saque que você desseja realizar "))

contaSamuel.SaqueBancario(valorSaque)
contaSamuel.ExibirDadosDaConta()

valorDeposito = float(input("Digite o valor de Deposito que você desseja realizar "))

contaSamuel.DepositoBancario(valorDeposito)



