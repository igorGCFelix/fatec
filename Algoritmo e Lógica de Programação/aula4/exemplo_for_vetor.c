//
// Created by lab53 on 15/04/2026.
# include <stdio.h>
#include <locale.h>

#define ex3

#ifdef ex1
int main () {
    int cont;
    for (cont=1;cont<=10;cont++) {
        printf("%d \n",cont);
    }
    return 0;
}
#endif

#ifdef ex2
//Receba cinco numeros quaisquer e armazene-o no vetor A que deverá ter cinco posições
int main() {
    int cont, A[5];

    for (cont=0;cont<=5;cont++) {
        printf("Digite um numero na posicao %d do vetor: ",cont);
        scanf("%d",&A[cont]);
    }


    for (cont=0;cont<=5;cont++)
        printf("Posicao %d: %d \n",cont, A[cont]);

    return 0;
}
#endif

#ifdef ex3
int main() {
    setlocale(LC_ALL,"Portuguese");
    int cont;
    float A[7];
    for (cont=1;cont<=7;cont++) {
        do {
            printf("Digite um numero na posicao %d: ",cont);
            scanf("%f",&A[cont]);
            if (A[cont]<0) {
                printf(("Digite novamente, número invalido \n"));
            }
        } while (A[cont]<0);
    }
    printf("Exibição do vetor:");
    for (cont=0;cont<=7;cont++) {
        printf("Posicao %d: %.2f\n",cont,A[cont]);
    }
}
