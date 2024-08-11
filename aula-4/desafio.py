# Desafio
# 1Vamos escrever um programa que recebe uma lista de produtos como argumento
# 2verifica se esses produtos estão disponíveis no mercado.
# 3 Se um produto estiver disponível, informaremos ao usuário quais produtos estão disponíveis e quais não estão.
# 4Além disso, exibiremos a lista de produtos disponíveis em ordem alfabética para referência futura.

produtosDisponiveis = ['Laranja', 'Suco', 'Carne', 'Refrigerante']
listaProdutos = []
produto = None
while True:
    produto = input('Digite o produto que deseja: (Digite 0 para finalizar)')
    if produto == '0':
        break
    if produto in produtosDisponiveis:
        listaProdutos.append(produto)
    else:
        print(f'O produto {produto} não está disponível')
print('Produtos disponíveis: ')
produtosDisponiveis.sort()
print(produtosDisponiveis)
print('Produtos comprados:')
print(listaProdutos)
