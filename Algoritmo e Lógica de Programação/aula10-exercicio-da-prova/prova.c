#include <stdio.h>
//
// Created by Igor on 5/21/2026.
//
int Dados[15];
void Armazena(int quantVal) {
    for (int i=0; i<quantVal; i++) {
        printf("\n Digite o %d valor do vetor: ", i+1);
        scanf("%d", &Dados[i]);
    }
}

int MaiorNumPositivo(int quantVal) {
    int maiorNum = 0, encontrou = 0;
    for (int i=0; i<quantVal; i++) {
        if(Dados[i] > 0) {

            if(encontrou == 0) {
                maiorNum = Dados[i];
                encontrou = 1;
            }
            else if(Dados[i] > maiorNum) {
                maiorNum = Dados[i];
            }
        }
    }

    if(encontrou == 0) {
        return -1;
    }

    return maiorNum;
}

int main() {
    int quantVal, maiorPositivo;
    do {
        printf("\n Digite a quantidade de dados que você deseja digitar (digite um valor entre 5 e 15): ");
        scanf("%d", &quantVal);
    }while (quantVal < 5 || quantVal > 15);

    Armazena(quantVal);
    maiorPositivo = MaiorNumPositivo(quantVal);

    if(maiorPositivo == -1) {
        printf("\nNao foi encontrado numero positivo no vetor.\n");
    }
    else {
        printf("\nMaior numero positivo encontrado: %d\n", maiorPositivo);
    }

    return 0;

}