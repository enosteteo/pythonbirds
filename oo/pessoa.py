class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'


class Mutante(Pessoa):
    olhos = 3

    def cumprimentar(self):
        return f'My name is {self.nome}'


class Homem(Mutante):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


if __name__ == '__main__':
    enos = Mutante(nome='Enos')
    ianka = Pessoa(nome='Ianka')
    iran = Homem(enos, ianka, nome='Iran')

    print(Pessoa.cumprimentar(iran))
    print(id(iran))
    print(iran.cumprimentar())
    print(iran.nome)
    print(iran.idade)
    for filho in iran.filhos:
        print(filho.nome)
    iran.sobrenome = 'Francisco'
    print(iran.sobrenome)
    print(f'{iran.nome} {iran.sobrenome}')
    del iran.filhos
    print(iran.__dict__)
    print(enos.__dict__)
    print(Pessoa.olhos)
    print(enos.olhos)
    print(id(ianka.olhos), id(enos.olhos), id(iran.olhos))
    print(Pessoa.metodo_estatico(), enos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), enos.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(enos, Pessoa))
    print(isinstance(enos, Homem))
    print(isinstance(pessoa, Homem))
    print(enos.olhos)
    print(ianka.cumprimentar())
    print(enos.cumprimentar())
    print(iran.cumprimentar())
