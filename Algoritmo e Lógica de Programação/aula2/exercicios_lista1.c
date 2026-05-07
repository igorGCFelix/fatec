// Exercicios da Lista 1
#include <math.h>
#include <string.h>
#include <stdio.h>
#define ex20

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

//testando string
#ifdef ex20
int main() {
    float n1, n2, n3, mediaEx, mediaFinal;
    int id;
    char conceito, situacao;

    do {
        printf("Digite o id do aluno: \n");
        scanf("%d", &id);
    }while (id < 0);

    do {
        printf("Digite a primeira nota do aluno: \n");
        scanf("%f", &n1);
    }while (n1<0 || n1 > 10);

    do {
        printf("Digite a segunda nota do aluno: \n");
        scanf("%f", &n2);
    }while (n2 < 0 || n2 > 10);

    do {
        printf("Digite a terceira nota do aluno: \n");
        scanf("%f", &n3);
    }while (n3 < 0 || n3 > 10);

    mediaEx = (n1 + n2 + n3) / 3;
    mediaFinal = (n1+ n2*2 + n3*3 + mediaEx)/7;

    if (mediaFinal <4) {
        conceito = "E";
        situacao = "Reprovado";
    }
    else if (mediaFinal <6){
        conceito = "D";
        situacao = "Aprovado";
    }
    else if (mediaFinal <7.5){
        conceito = "C";
        situacao = "Aprovado";
    }
    else if (mediaFinal <6){
        conceito = "B";
        situacao = "Aprovado";
    }
    else{
        conceito = "A";
        situacao = "Aprovado";
    }

    printf("Aluno de id: %d, tirou as notas: %.2f, %.2f, %.2f; tendo como média de exercícios: %.2f e média final de: %.2f. Sendo assim, esse aluno foi %c com a menção %c! ", id, n1, n2, n3, mediaEx, mediaFinal, situacao, conceito);
    return 0;

}
#endif