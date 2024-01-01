a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

#se tiver exatament o mesmo {} e valores, o a={} corresponderia ao a='AAAAA'. Pode ser usado indexes tbm 
#nome1 - parametro / c eh argumento 
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
