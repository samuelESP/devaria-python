def boasVinda(nome):
    print(f'Seja bem vindo {nome}')

if __name__ == '__main__':
    for n in range(0, 3):
        print(f'O número é {n}')

    for n in range(5, 0, -1):
        print(f'O número é {n}')

    for n in range(0, 10, 2):
        print(f'O número é {n}')

    palavra = 'devaria'
    for letra in palavra:
        print(f"A letra é {letra}")

    pessoas = ['samuel', 'valeria', 'matheus', 'victor', 'maria', 'daniel', 'daniela']
    for pessoa in pessoas:
        print(f"A pessoa é {pessoa}")

    for i, pessoa in enumerate(pessoas, 0) :
        print(f"A pessoa é {pessoa}, com o index de {i}")

    for pessoa in pessoas:
        boasVinda(pessoa)

    temCarroNaFila = True
    while temCarroNaFila:
        print(f'Lavando carro...')
        temCarroNaFila= False

    contador = 0;

    while contador <= 3:
        print(f'Meu contador está na posição {contador}')
        contador += 1
    else:
        print(f'Terminei de contar')