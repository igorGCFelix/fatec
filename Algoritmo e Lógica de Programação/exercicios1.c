#include<stdio.h>
int main() {
    int k, num, soma=0, numPositivo=0;
    float media;
    printf("Digite o número de vezes que você deseja inserir um valor: ");
    scanf("%i", &k);
    do{
        printf("Digite um número maior do que 0.");
    }
    while(k>0);

    printf("Digite um número");
    scanf("%i", &num);
    for (int cont=0; cont<k;cont++ ) {
        if (num>0) {
            soma = soma + num;
            numPositivo++;
        }

    }

    if (numPositivo>0) {
        media = soma/numPositivo;
        printf("Foram digitados %i. A média dos números positivos digitados é %f", numPositivo, media);
        return 0;
    }
    else {
        printf("Não foi digitado nenhum número positivo.");
        return 0;
    }




}