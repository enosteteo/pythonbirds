class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Eita', 24)
    print(p)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.idade)
    print(p.nome)
    p.nome = 'Enos'
    print(p.nome)
    print(p)
