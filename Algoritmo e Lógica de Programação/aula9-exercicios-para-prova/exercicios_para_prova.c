//
// Created by Igor on 5/19/2026.
//
#include <stdio.h>

#define ex2
#ifdef ex1
float notas[5];

void preencherNotas()
{
    for (int i = 0; i < 5; i++)
    {
        do
        {
            printf("Digite a nota do aluno %d: \n", i + 1);
            scanf("%f", &notas[i]);
        } while (notas[i] < 0 || notas[i] > 10);
    }
}

float calcularMedia()
{
    float soma, media;
    for (int i = 0; i < 5; i++)
    {
        soma += notas[i];
    }
    media = soma / 5;
    return media;
}

float mostrarMaiorNota()
{
    float maiorNota = notas[0];
    for (int i = 0; i < 5; i++)
    {
        if (notas[i]>maiorNota){
            maiorNota=notas[i];
        }
    }
    return maiorNota;
}

float contarAcimaMedia(float media)
{
    int cont=0;
    for(int i=0; i<5; i++){
        if(notas[i]>media){
            cont++;
        }
    }
    return cont;
}

int main(){
    preencherNotas();
    float media = calcularMedia();
    mostrarMaiorNota();
    int acimaMedia = contarAcimaMedia(media);

    printf("\n A média dos alunos foi de %.2f", media);
    printf("\n Teve %d alunos que tiraram uma nota acima da média", acimaMedia);
    
    return 0;
}
#endif

#ifdef ex2
int estoque[6];

void preencherEstoque(){
    for (int i=0; i<6; i++){
        do{
            printf("Digite a quantidade do produto número %d: \n", i+1);
            scanf("%d", &estoque[i]);
        }while(estoque[i]<0);

    }
}

int calcularTotalEstoque(){
    int totalEstoque=0;
    for (int i=0; i<6; i++){
        totalEstoque+=estoque[i];
    }
    return totalEstoque;
}

int mostrarMenorEstoque(){
    int menor=estoque[0];
    for (int i=0; i<6; i++){
        if (estoque[i]<menor){
            menor=estoque[i];
        }
    }
    return menor;
}

int contarEstoqueBaixo(){
    int cont=0;
    for (int i=0; i<6; i++){
        if (estoque[i]<10){
            cont++;
        }
    }
    return cont;
}

int main(){
    preencherEstoque();
    printf("\n O total de itens no estoque é: %d", calcularTotalEstoque());
    printf("\n O produto com menor quantidade de unidades no estoque possui %d unidade(s).", mostrarMenorEstoque());
    printf("\n %d produtos estão com o estoque baixo",contarEstoqueBaixo());

    return 0;
}
#endif