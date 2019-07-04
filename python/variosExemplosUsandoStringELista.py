palavra='T|:=eStE'
letras=[]
maiusculo=[]
minusculo=[]
letras.extend(palavra)	#transforma a string em uma lista(separa as letras da string)
print('palavra:',palavra)
print('letras:',letras)
maiusculo[:] = letras[:]	#faz cópia (usa [:] senão só é feito um aponteiramento)
minusculo[:] = letras[:]	#faz cópia (usa [:] senão só é feito um aponteiramento)
print('maiusc:',maiusculo)
print('minusc:',minusculo,'\n')
#----------------------------------tira as letras minusculas
for i in range(8):			
	if (maiusculo[i].islower()):
		maiusculo[i] = maiusculo[i].replace(maiusculo[i], '')
print('maiusc:',maiusculo)
#----------------------------------tira as letras maiusculas
for i in range(8):
	if (minusculo[i].isupper()):
		minusculo[i] = minusculo[i].replace(minusculo[i], '')
print('minusc:',minusculo)

print('\n\nsó letras:', maiusculo[1].isalpha())	#testa se é uma letra se nao for da false como resultado
minusculo = ''.join(minusculo)	#transforma a lista em uma string usando '' como separador dos elementos da lista na string
print('tamanho:', len(palavra))	#calcula o numero de caracteres na variavel
print('minusc:',minusculo,'\n')
print('tamanho:', len(minusculo))	#calcula o numero de caracteres na variavel
