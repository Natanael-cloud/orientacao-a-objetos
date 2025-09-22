class Conta:
    def __init__(self, saldo=0, nro_agencia=0, nro_conta=0):
        self._saldo = saldo
        self._nro_agencia = nro_agencia
        self._nro_conta = nro_conta

    # Getter para saldo
    @property
    def saldo(self):
        return self._saldo

    # Setter para saldo
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Erro: saldo não pode ser negativo!")
        else:
            self._saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Erro: valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
        elif valor > self._saldo:
            print("Erro: saldo insuficiente para saque.")
        else:
            print("Erro: valor de saque deve ser positivo.")
    
    def __str__(self):
        return f"Agência: {self._nro_agencia}, Conta: {self._nro_conta}, Saldo: R$ {self._saldo:.2f}"

# Teste da classe
conta = Conta(100, 1234, 56789)
conta.depositar(100)
print(conta.saldo)  # Exibe o saldo atual
conta.sacar(50)
print(conta.saldo)  # Exibe o saldo após o saque
print(conta)  # Exibe a visualização completa da conta
