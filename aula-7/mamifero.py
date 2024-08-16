from Animal import Animal
class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def amamentar(self):
        print(f'O animal {self.nome} é capaz de amamentar')