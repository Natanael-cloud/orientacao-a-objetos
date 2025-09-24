from abc import ABC, abstractmethod  # Importando o abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("TV Ligada")

    def desligar(self):
        print("Desligando a TV...")
        print("TV Desligada")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ar Condicionado Ligado")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar Condicionado Desligado")

    @property
    def marca(self):
        return "Samsung"
    

# Testando o Controle da TV
controle_tv = ControleTV()  # Criando uma instância da classe ControleTV
controle_tv.ligar()         # Chamando o método ligar
controle_tv.desligar()      # Chamando o método desligar
print(controle_tv.marca)    # Acessando o atributo 'marca' da TV

# Testando o Controle do Ar Condicionado
controle_ac = ControleArCondicionado()  # Criando uma instância da classe ControleArCondicionado
controle_ac.ligar()                     # Chamando o método ligar
controle_ac.desligar()                  # Chamando o método desligar
print(controle_ac.marca)                 # Acessando o atributo 'marca' do Ar Condicionado
