//
// Created by lab53 on 15/04/2026.
//
#include <stdio.h>

int main () {
    int cont, A[5];
    for (cont=0;cont<5;cont++) {
        printf("Digite um numero na posicao %d: \n",cont);
        scanf("%i", &A[cont]);

    }
    printf("Exibicao do vetor A\n");
    for (cont=0; cont<5;cont++) {
        printf("-%d, \n", A[cont]);
    }

}
//
