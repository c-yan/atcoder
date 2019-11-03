#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
    ll N, T;
    cin >> N >> T;
    vector<ll> t(N);
    rep(i, N) cin >> t[i];

    ll X = 0;
    for (int i = 1; i < N; i++) {
        X += min(t[i] - t[i - 1], T);
    }
    X += T;

    cout << X << endl;
    return 0;
}
