// Exercicios da Lista 1
#include <math.h>
#include<stdio.h>
#define ex19

#ifdef ex17
int main() {
    float salarioAnterior, salarioNovo;

    do {
        printf("Digite o salário antigo do funcionário: ");
        scanf("%f", &salarioAnterior);
    } while (salarioAnterior <= 0);

    if (salarioAnterior<800) {
        salarioNovo = salarioAnterior*1.15;
    }
    else if (salarioAnterior<=1000) {
        salarioNovo = salarioAnterior*1.1;
    }
    else {
        salarioNovo = salarioAnterior*1.05;
    }
    printf("O salario anterior era: %.2f reais, agora o salário novo é: %.2f reais.", salarioAnterior, salarioNovo);
}
#endif

#ifdef ex18
int main() {
    float n1, n2, n3, n4, media;

    printf("---- Seja bem vindo ao calculador de notas do Felix ----\n");

    do {
        printf("Digite a primeira nota: ");
        scanf("%f", &n1);
    }while (n1 < 0 || n1 > 10);

    do {
        printf("Digite a segunda nota: ");
        scanf("%f", &n2);
    }while (n2 < 0 || n2 > 10);

    do {
        printf("Digite a terceira nota: ");
        scanf("%f", &n3);
    }while (n3 < 0 || n3 > 10);

    do {
        printf("Digite a quarta nota: ");
        scanf("%f", &n4);
    }while (n4 < 0 || n4 > 10);

    media = (n1 + n2 + n3 + n4) / 4;

    printf((media >= 6) ? "Aluno aprovado!" : "Aluno reprovado!");

}
#endif

#ifdef ex19
int main() {
    int n1, n2, n3, n4;
    float resFinal;

    do {
        do {
            printf("\n Digite o primeiro número: ");
            scanf("%d", &n1);
        }while (n1<10 || n1>25);

        do {
            printf("Digite o segundo número: ");
            scanf("%d",&n2);
        }while (n2<0);

        n3 = n1 + n2;
        n4= n1*n2*n3;
        resFinal = pow(n1,2) + pow(n2,2) + pow(n3,2) + pow(n4,2);
        printf("%.2f", resFinal);
    } while (resFinal < 50000);

    return 0;

}
#endif