# Python Trata Tudo como Objeto
# As Classes em Python serão fábricas de Objetos
# Em toda classe haverá um construtor, métodos e atributos
# Python não precisa definir o tipo do Objeto


class Funcionario:
    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pagamento = pagamento
        self.email = nome + '.' + sobrenome + '@empresa.com'

