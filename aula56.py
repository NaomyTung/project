"""
split e join com list e str
split - divide uma string (list) - por default eh por espaco 
join - une uma string entre os items de uma lista iteravel 
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')
print (lista_frases_cruas)
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
