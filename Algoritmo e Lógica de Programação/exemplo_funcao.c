//
// Created by lab53 on 29/04/2026.
//
#include <stdio.h>
#include <locale.h>
#define ex3

#ifdef ex1
//Variável global
int X[5];

//Função armazena
int Armazena() {
    int cont;
    for (cont=0; cont<5; cont++) {
        printf("Digite na Posição %d\n", cont);
        scanf("%d", &X[cont]);
    }

}

//Função soma
//*int* Soma -> o int diz que tipo de dado a função irá retornar
int Soma() {
    int cont, soma=0;
    for (cont=0; cont<5; cont++) {
        if (X[cont]%2==0) {
            soma+=X[cont];
        }

    }
    if (soma==0) {
        printf("Nâo foi digitado nenhum número par no vetor X\n");
    }
    else {
        printf("A soma dos números pares positivos sâo %d \n",soma);
    }

}

float Media() {
    int cont, soma=0, cont5=0;
    float media;
    for (cont=0; cont<5; cont++) {
        if (X[cont]%5==0) {
            soma+=X[cont];
            cont5++;
        }

    }
    media=soma/cont5;
    printf("A média dos números múltiplos de 5 é: %.2f \n",media);
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    Armazena();
    Soma();
    Media();
}

#endif

#ifdef ex2
//Armazene na variavel global X cinco numeros quaisquer.
//Crie a função Armazena para guardar os numeros no vetor X.
//Crie a função Soma para calcular e exibir o resultado obtido na função Soma no interior da função Main.
//Crie a função Media para calcular a media de números múltiplos de 5
//Observação: Variaveis Globais SOMENTE VETORES

//Variável global
int X[5];

//Função armazena
int Armazena() {
    int cont;
    for (cont=0; cont<5; cont++) {
        printf("Digite na Posição %d\n", cont);
        scanf("%d", &X[cont]);
    }

}

//Função soma
int Soma() {
    int cont, soma=0;
    for (cont=0; cont<5; cont++) {
        if (X[cont]%2==0) {
            soma+=X[cont];
        }

    }
    return soma;


}

int Media() {
    int cont, soma=0, cont5=0;
    float media;
    for (cont=0; cont<5; cont++) {
        if (X[cont]%5==0) {
            soma+=X[cont];
            cont5++;
        }

    }
    media=soma/cont5;
    printf("A média dos números múltiplos de 5 é: %.2f \n",media);
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    Armazena();
    //atrelando o valor retornado da função Soma() para uma variável soma
    int soma=Soma();
    Media();

    if (soma==0) {
        printf("Nâo foi digitado nenhum número par no vetor X\n");
    }
    else {
        printf("A soma dos números pares positivos sâo %d \n",soma);
    }
}

#endif

#ifdef ex3
//Transforme este exercício em três funções: Receba doze números positivos e armazene no vetor A.
//Após a alimentação de todos os números mostre apenas os números maiores que 121 que estão armazenados no vetor.
//Verifique e exiba no interior da função main o maior número encontrado neste vetor.

int A[12];

int Armazena() {
    for (int cont=0; cont<12; cont++) {
        do {
            printf("Digite o número da posição %d: \n", cont);
            scanf("%d", &A[cont]);
        }while (A[cont]<=0);

    }

}

int Mostra() {
    printf("--- Resultado de números maiores que 121 ---\n");
    int comNumerosMaiores121 = 0;
    for (int cont=0; cont<12; cont++) {
        if (A[cont]>121) {
            comNumerosMaiores121=1;
            printf("A[%d] = %d\n", cont, A[cont]);
        }

    }
    if (comNumerosMaiores121==0) {
        printf("Não há números maiores que 121\n");
    }

}

int MaiorNumero() {
    int maiorNumero=0;

    printf("\n--- Resultado do maior número ---\n");
    for (int cont=0; cont<12; cont++) {
        if (A[cont] == 0) {
            maiorNumero = A[cont];
        }
        else {
            maiorNumero = A[cont];
        }
    }
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    Armazena();
    Mostra();

    int maiorNumero = MaiorNumero();
    printf("O maior número do vetor é: %d\n", maiorNumero);
}
#endif