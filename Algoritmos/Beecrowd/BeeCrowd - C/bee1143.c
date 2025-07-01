#include <stdio.h>

int main() {

    int n;
    scanf("%d", &n);

    int numero_atual = 1;

    for (int i; i < n; i++) {
   

    printf("%d %d %d\n", numero_atual, numero_atual*numero_atual, numero_atual*numero_atual*numero_atual);

    numero_atual++;
    }
    return 0;
}