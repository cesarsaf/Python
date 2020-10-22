
class Pessoa:
    def __init__(self):
        self.nome = 'Luis'
        self.sobrenome = 'Souza'
        self.altura = '1,75'
        self.peso = '90kg'

    def acordando(self):
        print('Estou acordando.')

    def comendo(self):
        print('Estou comendo.')
        
    def vivendo(self):
        print('Estou vivendo.')

    def dormindo(self):
        print('Estou dormindo.')

    def __str__(self):
        return ('A classe Pessoa: \n {}\n {}\n {}\n {}\n'.format(self.nome, self.sobrenome, self.altura, self.peso))
