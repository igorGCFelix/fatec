#include<stdio.h>
#define ex3

#ifdef ex1
int main(){
    int  a, b, soma;
    printf("Digite dois números quaisquer\n ");
    scanf("%d %i", &a,&b);
    soma = a + b;
    printf("Soma= %i\n", soma);
    return 0;
}
#endif // ex1

#ifdef ex2
int main(){
    int a, ant, suc;
    printf("Digite um número\n");
    scanf("%i", &a);
    ant = a - 1;
    suc = a + 1;
    printf("O antecessor de %i = %i\n: ",a,ant);
    printf("O sucessor de %i = %i\n: ",a, suc);
    return 0;
}
#endif // ex2

#ifdef ex3
int main(){
    float valor, valorAcrescimo, valorDesconto;
    do {
        printf("Digite um número maior que zero \n");
        scanf("%f", &valor);
        if(valor<=0){
            printf("Querido usuário, digite apenas números positivos\n");
        }
    }
    while(preco<=0);
    valorAcrescimo = valor 1*1;
    valorDesconto = valor - (valor *0.15);
    printf("O valor com acréscimo é igual %.2f\n",valorAcrescimo);
    printf("O valor com desconto é igual %.2f\n",valorDesconto);

    return 0;
}
#endif // ex3
