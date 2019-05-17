texto = open('gramatica.txt', 'r')
arq = texto.readlines()
linha=0
while linha < 14:
	arq[linha] = arq[linha].rstrip('\n')
	print(arq[linha])
	linha=linha+1
