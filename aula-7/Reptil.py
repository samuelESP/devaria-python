from Animal import Animal


class Reptil(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def botarOvos(self):
        print(f'O animal {self.nome} consegue colocar ovos')