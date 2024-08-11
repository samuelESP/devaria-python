
pessoas = ['samuel', 'rafael', 'maria']

pessoas.append('lucas')
print(f'{pessoas}')

pessoas.remove('lucas')
print(f'{pessoas}')

pessoas.insert(1, 'felipe')
print(f'{pessoas}')

pessoas.sort()
print(f'{pessoas}')

quantidadeDepessoas = len(pessoas)
print(f'{quantidadeDepessoas}')

pessoas.append('samuel')
numeroDeSamuel = pessoas.count('samuel')
print(f'{numeroDeSamuel}')

pessoas.clear()
print(f'{pessoas}')


notasDosAlunos = [100, 80, 77, 40, 55, 60]

mediaDasnotasDosAlunos = lambda notas: sum(notas) / len(notas)
print(f'a media das notas dos Alunos é de {mediaDasnotasDosAlunos(notasDosAlunos)}')


#list(filter(lambda <argumento>: <expressão>, <lista>))
notasAcimaDeSetenta = list(filter(lambda i : i > 60, notasDosAlunos))
print(f'{notasAcimaDeSetenta}')
