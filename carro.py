
class Carro:
    def __init__(self):
        self.marca = 'Ford'
        self.modelo = 'Focus'
        self.valor = 50000
    
    def ligar(self):
        print('Estou ligando.')

    def andar(self):
        print('Estou andando.')

    def desligar(self):
        print('Estou desligando.')

    def __str__(self):
        return ('{}\n {}\n {}\n '.format(self.marca, self.modelo, self.valor))



