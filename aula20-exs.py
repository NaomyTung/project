primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(primeiro_valor, "eh maior que", segundo_valor)
elif segundo_valor > primeiro_valor:
    print(segundo_valor, "eh maior que", primeiro_valor)
else:
    print("valores sao iguais")


    ######segundo_valor= aparece nome da variavel igual ao valor que foi dado a ela 

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )   