//
// // Created by Andrews, Igor, Lucas
//
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <math.h>

//    Crie a função Esfera que receba da função main o valor do raio e calcule o volume da esfera o seu volume (v = 4/3*Pi*R3).
//    Exiba o resultado obtido no interior da função main.

float Esfera(float raio) {
    float volume;
    volume = 4*(3.14* pow(raio, 3) )/3;
    return volume;
}

int main () {
    float raio, volume;
    printf("Digite o raio da esfera:\n");
    scanf("%f",&raio);
    volume = Esfera(raio);

    printf("O volume é: %.2f\n", volume);
    return 0;
}
