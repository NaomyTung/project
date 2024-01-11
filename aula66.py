"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)

#argumento nomeado - melhor ou tudo ou nada nomeado - mas eh permitido misturar. Mas dps do que foi nomeado, todos precisam
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
