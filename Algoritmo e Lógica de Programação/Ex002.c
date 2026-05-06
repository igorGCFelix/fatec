//
// Created by lab53 on 06/05/2026.
// Exercício de funções 2
//Nomes dos integrantes: Andrews, Igor, Rafael
#include <stdio.h>
int vetorA[10];
int vetorB[10];
int Armazenar_A();

void Armazena_A(int quantVal) {
    for (int i = 0; i < quantVal; i++) {
        printf("\n Digite o %d valor do vetor A na posicao: ", i+1);
        scanf("%i", &vetorA[i]);
    }
}
int SomaPardeA(int quantVal) {
    int somaPar = 0;
    for (int i = 0; i < quantVal; i++) {
        if (vetorA[i]%2==0) somaPar = somaPar + vetorA[i];
    }
    return somaPar;
}
int SomaImpardeB (int quantVal) {
    int somaImpar = 0;
    for (int i = 0; i < quantVal; i++) {
        if (vetorB[i]%2==1) somaImpar = somaImpar + vetorB[i];
    }
    return somaImpar;
}
void Exiba(int quantVal, int vetor[]) {
    for (int i = 0; i < quantVal; i++) {
        printf("%d, ", vetor[i]);
    }
}

int main () {
    int somaPar, somaImpar;
    int quantVal;
    printf("Digite o numero de elementos que vao ser digitados no vetor (um valor entre 3 e 10): \n");
    scanf("%d", &quantVal);
    while (quantVal<3 || quantVal>10) {
        printf("VALOR INVALIDO. DIGITE UM NUMERO ENTRE 3 E 10 \n");
        printf("Digite o numero de elementos que vao ser digitados no vetor: \n");
        scanf("%d", &quantVal);
    }
    Armazena_A(quantVal);
    for (int i = 0; i < quantVal; i++) {
        vetorB[i] = vetorA[i]*5;
    }
    printf("\n Valores do vetor de A: ");
    Exiba(quantVal, vetorA);
    printf("\n Valores do vetor de B: ");
    Exiba(quantVal, vetorB);
    somaPar = SomaPardeA(quantVal);
    somaImpar = SomaImpardeB(quantVal);
    printf("\n A soma dos valores pares do vetor A eh igual a: %d", somaPar);
    printf("\n A soma dos valores impares do vetor B eh igual a: %d", somaImpar);
    return 0;
}

