class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando alto!")  # Implementação específica para Pardal
        super().voar()  # Chama o método da classe pai para manter a funcionalidade

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Andorinha(Passaro):
    def voar(self):
        print("Andorinha voando rápido!")

def plano_voo(obj):
    obj.voar()

# Instanciando os objetos
p1 = Pardal()
p2 = Avestruz()
p3 = Andorinha()

# Testando a função plano_voo com objetos diferentes
plano_voo(p1)  # Pardal voa
plano_voo(p2)  # Avestruz não pode voar
plano_voo(p3)  # Andorinha voa

