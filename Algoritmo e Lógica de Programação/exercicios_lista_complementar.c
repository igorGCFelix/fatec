// Exercicios da Lista Complementar
#include<stdio.h>
#define ex6

#ifdef ex6
int main() {
    int horas, horasExtras;
    float salarioBruto, imposto;
    do {
        printf("Digite o número anual de horas trabalhadas: ");
        scanf("%d", &horas);
    }while (horas <= 0);

    do {
        printf("Digite o número anual de horas extras trabalhadas: ");
        scanf("%d", &horasExtras);
    }while (horasExtras <= 0);

    salarioBruto = horas*10 + horasExtras*15;

    if (salarioBruto<=12000) {
        imposto = salarioBruto*0.1;
        printf("O imposto a ser pago é de: %.2f", imposto);
        return 0;
    }
    else {
        imposto = (salarioBruto-12000)*0.15 + 12000*0.1;
        printf("O imposto a ser pago de: %.2f", imposto);
        return 0;
    }

}
#endif
