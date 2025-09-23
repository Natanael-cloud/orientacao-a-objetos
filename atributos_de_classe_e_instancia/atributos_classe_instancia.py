class Estudante:
    escola = "DIO"  # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}"


# Criando instâncias de Estudante
aluno_1 = Estudante("Gilberto", 3)
aluno_2 = Estudante("Giovana", 2)

# Imprimindo os objetos
print(aluno_1)
print(aluno_2)
