from Quadrado import Quadrado
from Circulo import Circulo


formas = [
    Quadrado(),
    Circulo()
]

for forma in formas:
    forma.desenhar()