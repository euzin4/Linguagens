texto = open('gramatica.txt', 'r')	#abre o arquivo para leitura 'r'
arq = texto.readlines()			#arq vira um vetor com uma linha em cada posição
for linha in arq:			#for percorre todas as posições do vetor
	linha=linha.rstrip('\n')	#retira o caractere '\n' da variavel que será printada
	print(linha)			#printa a linha percorrida atual
print("----\n"+arq[0])			#printa através da posição do vetor
