#include <stdio.h>
#include <stdlib.h>

int main(){
	char string[255];

	memset(string, NULL, sizeof(string));
}

//1º Parâmetro: Um ponteiro para o primeiro byte da posição de memória em que a variavel está amazenada (nesse caso a "string").
//2º Parâmetro: É o valor que cada elemento irá receber.
//3º Parâmetro: É o número de bytes que cada elemento possui (o tamanho da variavel utilizada)

//Neste exemplo cada elemento do vetor string receberá o valor NULL.
