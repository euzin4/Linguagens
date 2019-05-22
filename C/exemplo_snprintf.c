#include <stdio.h>
#include <math.h>

int main(){
   char str[80];

   snprintf(str, sizeof(str), "Valor de Pi = %f", M_PI);
   puts(str);

   return(0);
}

//Ele pega uma string de formatação (cada % indica o lugar onde vai entrar uma variável) e vai substituindo os % pelas variaveis que vc vai passando.
//Ele funciona igual a printf, mas salva o resultado em um ponteiro. 
