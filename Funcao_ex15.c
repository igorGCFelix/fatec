#include <stdio.h>  
#include <string.h>
/*
Exercicio 14 da lista de funções sem vetores
Created by Lucas, Andrews, Igor
*/
// Utilização da biblioteca string.h para manipulação de strings e fgets para leitura de strings com espaços.
void Media(char nome[])
{
    float soma = 0.0, media, nota;
    int c;
    for (c = 0; c < 4; c++)
    {
        printf("digite a %i nota: ", c + 1);
        scanf("%f", &nota);
        if (nota < 0 || nota > 10)
        {
            while(nota < 0 || nota > 10)
            {
                printf("Nota invalida, digite novamente: ");
                scanf("%f", &nota);
            }
        }
        soma += nota;
    }
    media = soma / 4;
    printf("====== RESULTADO ======\n");
    printf("Aluno: %s\n", nome);
    printf("Media: %.2f\n", media);
    if (media >= 0.0 && media < 4.9)
    {
        printf("Conceito: D\n");
    }
    else if (media >= 5.0 && media < 6.9)
    {
        printf("Conceito: C\n");
    }
    else if (media >= 7.0 && media < 8.9)
    {
        printf("Conceito: B\n");
    }
    else if (media >= 9.0 && media <= 10.0)
    {
        printf("Conceito: A\n");
    }
    printf("=======================\n");
}

int main()
{
    char nome[100];
    int quantAluno;
    do
    {
        printf("Digite a quantidade de alunos: ");
        scanf("%i", &quantAluno);
        if (quantAluno < 3 || quantAluno > 50)
        {
            printf("Quantidade de alunos invalida, digite novamente.\n");
        }
    } while (quantAluno < 3 || quantAluno > 50);
    int c;
    while ((c = getchar()) != '\n' && c != EOF); // Limpa o buffer de entrada

    for (int i = 0; i < quantAluno; i++)
    {
        printf("Digite o nome do %dº aluno: ", i + 1);
        
        fgets(nome, sizeof(nome), stdin); // le o nome do aluno, permitindo espaços.
        // Verifica se o nome é vazio e solicita novamente.
        if (nome[0] == '\n') {
            printf("Nome vazio, digite novamente.\n");
            i--; 
            continue;
        }
        // Remove o caractere de nova linha do final da string, se presente.   
        size_t len = strlen(nome);
        if (len > 0 && nome[len-1] == '\n') {
            nome[len-1] = '\0';
        }
        Media(nome);
        while ((c = getchar()) != '\n' && c != EOF);
    }
    
    return 0;
}
