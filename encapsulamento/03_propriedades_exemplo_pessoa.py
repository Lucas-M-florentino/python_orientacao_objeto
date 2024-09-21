class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        __ano_atual = 2024
        return __ano_atual - self.__ano_nascimento

pessoa = Pessoa('Lucas', 1998)
print(pessoa.nome)
print(pessoa.idade)
