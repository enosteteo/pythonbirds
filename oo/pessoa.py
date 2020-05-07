class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    enos = Pessoa(nome='Enos')
    ianka = Pessoa(nome='Ianka')
    iran = Pessoa(enos, ianka, nome='Iran')

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
    enos.olhos = 2
    print(iran.__dict__)
    print(enos.__dict__)
    print(Pessoa.olhos)
    print(enos.olhos)
    print(id(ianka.olhos), id(enos.olhos), id(iran.olhos), )

