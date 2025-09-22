class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    # Getter para nome
    @property
    def nome(self):
        if self._nome is None:
            raise ValueError("O nome não pode ser None.")
        return self._nome
    
    # Getter para idade
    @property
    def idade(self):
        _ano_atual = 2025
        if self._ano_nascimento > _ano_atual:
            raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
        return _ano_atual - self._ano_nascimento

# Teste da classe
pessoa = Pessoa('Jose', 1993)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# Teste com erro (ano de nascimento maior que o ano atual)
# pessoa_errada = Pessoa('Maria', 2026)
# print(f"Nome: {pessoa_errada.nome} \tIdade: {pessoa_errada.idade}")

