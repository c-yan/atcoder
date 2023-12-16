#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;

    vector<int> result(N + 1);
    for(int x = 1; x < 101; x++) {
        for(int y = 1; y < 101; y++) {
            for(int z = 1; z < 101; z++) {
                int n = x * x + y * y + z * z + x * y + y * z + z * x;
                if (n > N) break;
                result[n]++;
            }
        }
    }

    for(int i = 1; i < N + 1; i++) {
        cout << result[i] << endl;
    }
}
