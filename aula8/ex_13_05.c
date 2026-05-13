//
// Created by lab53 on 13/05/2026.
//

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

#define ex1

#ifdef ex1
//Crie um programa dividido em funções:
//Guarde:declare localmente e receba no interior da função main a quantidade de
//números a ser armazenada no vetor X.O tamanho máximo do  vetor X é 20.
//Multiplica:calcule o produto dos números pares contidos no vetor X.Exiba o produto no interior
//da função main.
//MediaImpar:calcule e exiba no interior dessa função a média dos números impares contidos
//no vetor X.
//VetorPositivos:crie um vetor chamado Positivos para armazenar os numeros
// positivos contidos no vetor X.

int X[20], positivos[20];

void Guarde(int quantNumArmazenados) {
    setlocale(LC_ALL, "Portuguese");
    for (int i = 0; i < quantNumArmazenados; i++) {
        printf("\n Digite o número referente ao X[%d]: ", i);
        scanf("%d", &X[i]);
    }

}

int Multiplica(int quantNumArmazenados) {
    int produtosPares=1;
    for (int i = 0; i < quantNumArmazenados; i++) {
        if (X[i]%2 == 0) {
            produtosPares = X[i]*produtosPares;
        }
    }
    return produtosPares;
}

float MediaImpar(int quantNumArmazenados) {
    int somaImpares=0, cont=0;
    float media;
    for (int i = 0; i < quantNumArmazenados; i++) {
        if (X[i]%2 != 0) {
            somaImpares += X[i];
            cont++;
        }
    }
    if (cont==0) {
        printf("\n Não há números impares");
    }
    else {
        media = somaImpares/cont;
        printf("\n A média dos números ímpares é: %.2f", media);
    }

    return media;
}

int VetoresPositivos(int quantNumArmazenados) {
    printf("\n --- Vetores Positivos --- ");
    int cont=0;
    for (int i = 0; i < quantNumArmazenados; i++) {
        if (X[i]>0) {
            positivos[i] = X[i];
            printf("\n X[%d]: %d", i, X[i]);
            cont++;
        }
    }
    if (cont==0) {
        printf("Não há números positivos");
    }
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int quantNumArmazenados;
    do {
        printf("Digite a quantidade de números que deseja armazenar: ");
        scanf("%d", &quantNumArmazenados);
    }while (quantNumArmazenados < 0 || quantNumArmazenados > 20);

    Guarde(quantNumArmazenados);
    printf("O produto de números pares é: %d", Multiplica(quantNumArmazenados));
    MediaImpar(quantNumArmazenados);
    VetoresPositivos(quantNumArmazenados);
}

#endif


