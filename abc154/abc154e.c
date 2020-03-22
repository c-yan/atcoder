#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char N[200];
static char tmp[10];
static int b[4];

int main() {
    fgets(N, sizeof(N), stdin);
    fgets(tmp, sizeof(tmp), stdin);
    int K = atoi(tmp);

    int a = 1;

    b[0] = 1;
    b[1] = N[0] - '1';

    for (int i = 1; i < strlen(N) - 1; i++) {
        int t = N[i] - '0';
        for (int j = K - 1; j > -1; j--) {
            b[j + 1] += b[j] * 9;
        }
        if (t != 0) {
            if (a + 1 <= K) b[a + 1] += t - 1;
            if (a <= K) b[a] += 1;
            a++;
        }
    }

    printf("%d\n", b[K] + (a == K ? 1 : 0));
}
