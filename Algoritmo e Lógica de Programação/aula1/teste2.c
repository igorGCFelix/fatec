int main(void)
{
    int a;
    int b;
    int soma;
    int repeticao;

    do
    {
        printf("Digite o primeiro número:");
        scanf("%d", &a);

        printf("Digite o segundo número:");
        scanf("%d", &b);

        soma = a + b;
        printf("O resultado da soma é: %d\n", soma);
        printf("Digite 1 para continuar ou 2 para sair\n");
        scanf("%d", &repeticao);
    }
    while (repeticao==1);
    return 0;
}
