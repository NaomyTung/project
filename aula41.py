""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        #quando tem break dentro do while, o else nao eh executado 
        # toda vex que o while chegar ao final, vai fazer o else 
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
