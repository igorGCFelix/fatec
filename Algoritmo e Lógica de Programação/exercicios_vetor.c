#include <stdio.h>
#include <locale.h>
#define ex1

#ifdef ex1
//Armazene no vetor A 7 números positivos e exiba a soma de todos os numeros armazenados no vetor.
int main () {
    setlocale (LC_ALL,"Portuguese");
    int cont;
    float A[7], soma=0;

    for (cont=0;cont<7;cont++) {
        do {
            printf("Digite um numero para a posição %i: ", cont);
            scanf("%f", &A[cont]);
        }while (A[cont]<=0);
        soma= soma + A[cont];
    }
    printf("A soma dos valores alocados ao vetor é: %.2f", soma);
    return 0;
}
#endif