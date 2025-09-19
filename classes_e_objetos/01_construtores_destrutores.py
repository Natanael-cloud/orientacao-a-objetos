class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        print(f"Cachorro {self.nome} criado.")

    def __del__(self):
        print(f"Removendo as instâncias da classe Cachorro: {self.nome}")

    def latir(self):
        print("Latindo: AU AU")

    def __str__(self):
        return f"{self.__class__.__name__} nome={self.nome}, cor={self.cor}, acordado={self.acordado}"


# Criando o objeto
c = Cachorro("Rex", "marrom")
c.latir()

# Exibindo a representação do cachorro
print(c)  # Exibindo as informações do cachorro usando __str__
