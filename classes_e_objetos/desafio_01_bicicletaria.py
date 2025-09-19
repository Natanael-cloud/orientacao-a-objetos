class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando: BIP BIP")

    def parar(self):
        print("A bicicleta parou.")

    def acelerar(self):
        print("Acelerando a bicicleta.")

    def __str__(self):
        return f"{self.__class__.__name__} cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

# primeiro objeto
b1 = Bicicleta("vermelha", "caloi", 2020, 1200)
b1.buzinar()
b1.acelerar()
b1.parar()  
print(b1)  # Exibindo a representação da bicicleta usando __str__

# segundo objeto
b2 = Bicicleta("azul", "monark", 2019, 800)
b2.buzinar()
b2.acelerar()
b2.parar()
print(b2)  # Exibindo a representação da bicicleta usando __str__


 #Saída esperada:
# Buzinando: BIP BIP
#Acelerando a bicicleta.
#A bicicleta parou.
# Bicicleta cor=vermelha, modelo=caloi, ano=2020, valor=1200

