#include <atcoder/all>
#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using ll = long long;
using namespace std;
using namespace atcoder;

int main()
{
    int N, Q;
    cin >> N >> Q;

    dsu d(N);
    rep(_, Q) {
        int t, u, v;
        cin >> t >> u >> v;
        if (t == 0) {
            d.merge(u, v);
        } else if (t == 1) {
            if (d.same(u, v)) {
                cout << "1" << '\n';
            } else {
                cout << "0" << '\n';
            }
        }
    }
    cout << endl;

    return 0;
}
