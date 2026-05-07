#include <stdio.h>
#include <locale.h>
#include <windows.h>

#define ex4

#ifdef ex1
//Armazene no vetor A 7 n?meros positivos e exiba a soma de todos os numeros armazenados no vetor.
int main () {
    setlocale (LC_ALL,"Portuguese");
    int cont;
    float A[7], soma=0;

    for (cont=0;cont<7;cont++) {
        do {
            printf("Digite um numero para a posição %i do vetor: ", cont);
            scanf("%f", &A[cont]);
        }while (A[cont]<=0);
        soma= soma + A[cont];
    }
    printf("A soma dos valores alocados ao vetor ?: %.2f", soma);
    return 0;
}
#endif

#ifdef ex2
//Leia quinze elementos de um vetor. Ap?s a alimenta??o mostre todos os elementos armazenados no vetor
int main() {
    setlocale (LC_ALL,"Portuguese");
    float A[15];

    for (int cont=0;cont<15;cont++) {
        printf("Digite um numero na posicao %d do vetor: ",cont);
        scanf("%f",&A[cont]);
    }

    for (int cont=0;cont<15;cont++) {
        printf("Posicao %d: %2.f \n",cont, A[cont]);
    }

    return 0;
}

#endif

#ifdef ex3
//Receba doze n?meros positivos e armazene no vetor A. Ap?s a alimenta??o de todos os n?meros, mostre apenas os n?meros maiores que 121 que est?o armazenados no vetor
int main() {
    //setlocale (LC_ALL,".UTF-8");
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);

    float A[12];
    for(int i=0;i<12;i++) {
        do {
            printf("Digite o um número positivo para a positivo %i do vetor: ",i);
            scanf("%f", &A[i]);
        }while (A[i]<=0);

    }
    printf("Valores alocados no vetor: ");
    for (int i=0;i<12;i++) {
        if (A[i]>121) {
            printf("Posicao %i: %2.f \n", i, A[i]);
        }
    }
    return 0;
}

#endif

#ifdef ex4
//Leia oito elementos e armazene-os no vetor A. Construa o vetor B de mesma dimensão com os elementos do vetor A multiplicados por
// 3. Apresente os conteúdos dos dois vetores.
int main() {
    setlocale (LC_ALL,"Portuguese");
    float A[8], B[8]; //elementos do vetor A multiplicados por 3
    for (int cont=0; cont<8;cont++) {
        printf("Digite um número: ");
        scanf("%f", &A[cont]);
    }
    printf("--- Resultados dos vetores ---\n");
    for (int cont=0; cont<8; cont++) {
        B[cont]= A[cont] * 3;
        printf("A[%i] = %.2f\n B[%i] = %.2f\n\n", cont, A[cont], cont, B[cont]);
    }
    return 0;
}
#endif