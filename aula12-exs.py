... #chamado de ellipsis, usado como placeholder

nome = 'Naomy'
altura = 1.55
peso = 51
imc = peso / altura ** 2

print(nome + " tem " + str(altura) + " de altura,")
print("pesa " + str(peso) + " quilos e seu IMC e")
print(imc)

##outra solucao 
print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)