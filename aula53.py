"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# o enumerate vai criar comecar c zero por default, e vai criar
    #para cada item um numero e o que esta na lista em uma tupla
# python ja sabe que vc quere desempactar, e pegar o indice e nome
# da tupla, por isso vc pd usar direto duas vars in enumerate (lista). 

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')


lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)
#se fizer de novo, o iterator ja esta zerado, ent esgota e n mostra nada
for item in lista_enumerada:
    print(item)

# para resolver, criar um iterator por vez. 
#O enumerate, enumera os valores de cada index
for item in enumerate(lista):
    print(item)