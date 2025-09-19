class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"O motor do veículo {self.placa} está ligado.")

    def __str__(self):
        return f"{self.__class__.__name__} cor={self.cor}, placa={self.placa}, numero_rodas={self.numero_rodas}"


class Motocicletas(Veiculos):
    def __init__(self, cor, placa):
        super().__init__(cor, placa, 2)  # Motocicletas têm 2 rodas

    def buzinar(self):
        print("Motocicleta buzinando: BIP BIP")


class Carros(Veiculos):
    def __init__(self, cor, placa):
        super().__init__(cor, placa, 4)  # Carros têm 4 rodas

    def buzinar(self):
        print("Carro buzinando: BEEP BEEP")


class Caminhoes(Veiculos):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, o caminhão está carregado.")

    def buzinar(self):
        print("Caminhão buzinando: HOOONK HOOONK")

    def __str__(self):
        return super().__str__() + f", carregado={self.carregado}"


# Criando instâncias das classes e testando os métodos
moto = Motocicletas("Vermelha", "ABC1234")
moto.ligar_motor()
moto.buzinar()
print(moto)

carro = Carros("Azul", "XYZ5678")
carro.ligar_motor()
carro.buzinar()
print(carro)

caminhao = Caminhoes("Branco", "DEF9012", 6, True)
caminhao.ligar_motor()
caminhao.buzinar()
caminhao.esta_carregado()
print(caminhao)
