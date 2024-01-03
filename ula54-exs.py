"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
#import os

#os.system("clear")

# ctrl + / para comentar

# after except it goes to the next thing after the try catch.
# if I put the continue after that, it will just go through the loop again  

lista_compras = []

while True:
    print("Selecione uma opcao")
    user_choice = input('[i]nserir [a]pagar [l]istar: ').lower()
    if(user_choice == 'i'):
        new_item = input('Inser new item: ').lower()
        lista_compras.append(new_item)
    elif(user_choice == 'a'):
        delete_item = input('Index to delete: ')
        try:
            delete_item = int(delete_item)
            lista_compras.pop(delete_item)
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
        # print("test try-catch flow")
    elif(user_choice == 'l'):
        for i, item in enumerate(lista_compras):
            print(i, item)
    else:
        print("Not a valid enter")




###########outra solucao professor 
        """
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
