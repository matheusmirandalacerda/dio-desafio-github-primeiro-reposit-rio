from tkinter.filedialog import SaveFileDialog


class Conta:
    def __init__(self, nro_agencia , saldo = 0):

        self._saldo = saldo 
        self.nro_agencia = nro_agencia

    def depositar(self,valor):

        self._saldo += valor

    def sacar(self,valor):

        self._saldo -= valor

    def mostrar_saldo(self):

        return self._saldo

conta = Conta("0001", 100)
# conta._saldo += 100 Aqui ele está manipulando o saldo, mas o correto é realizar o depósito ou saque
conta.depositar(100)
print(conta._saldo) # mesma coisa da função mostra_saldo
print(conta.nro_agencia)
print(conta.mostrar_saldo()) 