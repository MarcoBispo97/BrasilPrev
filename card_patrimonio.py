from random import randint


class Patrimonio:

    def __init__(self, id, type_of_estrategia=None, *args, **kwargs):
        self.id = id
        self.type_of_estrategia = type_of_estrategia
        self.rental_preco = randint(30, 120)
        self.propriedade_preco = randint(30, 120)

    def __repr__(self):
        return f'''
            id:{self.id}
            type_of_estrategia:{self.type_of_estrategia}
            rental_preco:{self.rental_preco}
            propriedade_preco:{self.propriedade_preco}
        '''

    def __str__(self):
        return f'''
            id:{self.id}
            type_of_estrategia:{self.type_of_estrategia}
            rental_preco:{self.rental_preco}
            propriedade_preco:{self.propriedade_preco}
