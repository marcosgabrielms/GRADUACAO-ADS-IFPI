#include <stdio.h>

int main () {
    
    int n;
    scanf("%d", &n);
    
    int contador_global = 1;
    
    for (int i; i < n; i++) {
        printf("%d %d %d PUM\n", contador_global, contador_global + 1, contador_global + 2);
        
        contador_global += 4;
    }
    return 0;
}