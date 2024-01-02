"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez 
iter -> me entregue seu iterador
next -> me entregue o próximo valor

"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)