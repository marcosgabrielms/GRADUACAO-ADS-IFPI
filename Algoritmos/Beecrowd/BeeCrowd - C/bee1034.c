#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_M 1000001

int fila[MAX_M];
int passos[MAX_M];
bool visitado[MAX_M];

int bfs(int blocos[], int n, int m) {
    int inicio = 0, fim = 0;

    for (int i = 0; i <= m; i++) {
        visitado[i] = false;
        passos[i] = 0;
    }

    fila[fim++] = 0;
    visitado[0] = true;

    while (inicio < fim) {
        int atual = fila[inicio++];

        if (atual == m) return passos[atual];

        for (int i = 0; i < n; i++) {
            int proximo = atual + blocos[i];
            if (proximo <= m && !visitado[proximo]) {
                visitado[proximo] = true;
                passos[proximo] = passos[atual] + 1;
                fila[fim++] = proximo;
            }
        }
    }

    return -1;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);

        int blocos[25];
        for (int i = 0; i < n; i++) {
            scanf("%d", &blocos[i]);
        }

        printf("%d\n", bfs(blocos, n, m));
    }

    return 0;
}
