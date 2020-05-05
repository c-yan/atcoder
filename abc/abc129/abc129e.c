#include <stdio.h>
#include <string.h>

int main() {
     char L[100100];
     fgets(L, sizeof(L), stdin);

     long long result = 1;
     long long t = 1;
     for(int i = strlen(L) - 2; i >= 0; i--) {
         if (L[i] == '1') {
             result = result * 2 + t;
             result %= 1000000007;
         }
         t *= 3;
         t %= 1000000007;
     }
     printf("%lld\n", result);
}
