#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using ll = long long;
using namespace std;

#define MAX_N 17
#define INF 2147483647

ll N;
ll dp[1 << MAX_N][MAX_N];
ll d[MAX_N][MAX_N];

void solve() {
    rep(i, 1 << N) rep(j, N) dp[i][j] = INF;
    dp[(1 << N) - 1][0] = 0;

    for (int S = (1 << N) - 2; S >= 0; S--) {
        for (int v = 0; v < N; v++) {
            for (int u = 0; u < N; u++) {
                dp[S][v] = min(dp[S][v], dp[S | 1 << u][u] + d[v][u]);
            }
        }
    }
    cout << dp[0][0] << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    vector<ll> X(N), Y(N), Z(N);
    rep(i, N) {
        cin >> X[i] >> Y[i] >> Z[i];
    }

    rep(i, N) {
        rep(j, N) {
            d[i][j] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]) + max(0ll, Z[i] - Z[j]);
        }
    }

    solve();

    return 0;
}
