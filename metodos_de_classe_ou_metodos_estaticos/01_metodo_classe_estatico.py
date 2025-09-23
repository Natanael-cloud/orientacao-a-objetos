class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano  
        return cls(nome, idade)  
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18  

# Criando uma instância de Pessoa usando o método de classe
p = Pessoa().criar_apartir_data_nascimento(1994, 12, 26, "Natan")
print(p.nome, p.idade)  # Saída: "Natan 31" porque a idade foi calculada com base no ano de nascimento

# Verificando se a pessoa com 18 anos é maior de idade
print(Pessoa.e_maior_idade(18))  # Saída: True, porque 18 é maior ou igual a 18

# Verificando se a pessoa com 8 anos é maior de idade
print(Pessoa.e_maior_idade(8))  # Saída: False, porque 8 não é maior ou igual a 18

