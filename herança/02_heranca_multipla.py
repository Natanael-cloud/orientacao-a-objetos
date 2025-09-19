class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, nro_patas, **kwargs):
        super().__init__(nro_patas)  # Chama o construtor da classe Animal
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, nro_patas, **kwargs):
        super().__init__(nro_patas)  # Chama o construtor da classe Animal
        self.cor_bico = cor_bico

class Gato(Mamifero):
    def __init__(self, nro_patas, cor_pelo):
        super().__init__(cor_pelo, nro_patas)

class Ornintorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        Mamifero.__init__(self, cor_pelo, nro_patas)  # Chama o construtor de Mamifero
        Ave.__init__(self, cor_bico, nro_patas)  # Chama o construtor de Ave

# Criando instâncias e testando
gato = Gato(4, "Laranja")
print(gato)

ornintorrinco = Ornintorrinco(4, "Marrom", "Laranja")
print(ornintorrinco)

print(Ornintorrinco.__mro__)  # Mostra a ordem de resolução de métodos (MRO)
