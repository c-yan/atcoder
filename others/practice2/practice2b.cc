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

    fenwick_tree<ll> ft(N);
    rep(i, N) {
        int a;
        cin >> a;
        ft.add(i, a);
    }

    rep(_, Q) {
        int t;
        cin >> t;
        if (t == 0) {
            int p, x;
            cin >> p >> x;
            ft.add(p, x);
        } else if (t == 1) {
            int l, r;
            cin >> l >> r;
            cout << ft.sum(l, r) << '\n';
        }
    }
    cout << endl;

    return 0;
}
