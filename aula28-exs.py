#Exercício
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    #p_letra = nome[0]
    #u_letra = nome[len(nome)-1]
    print(f'Seu nome eh {nome}')
    print(f'Seu nome invertido eh {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')
else:
    print ("Desculpe, você deixou campos vazios.")
