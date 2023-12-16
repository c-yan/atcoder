#include <atcoder/all>
#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using ll = long long;
using namespace std;
using namespace atcoder;

ll op(ll a, ll b) { return a + b; }

ll e() { return 0; }

int main()
{
    ll Q;
    cin >> Q;

    segtree<ll, op, e> st(200000);
    rep(_, Q) {
        ll T, X;
        cin >> T >> X;
        if (T == 1) {
            st.set(X - 1, 1);
        } else if (T == 2) {
            ll ok = 200000;
            ll ng = 0;
            while (ok - ng > 1) {
                ll m = ng + (ok - ng) / 2;
                if (st.prod(0, m) >= X) {
                    ok = m;
                } else {
                    ng = m;
                }
            }
            cout << ok << '\n';
            st.set(ok - 1, 0);
        }
    }
    cout << flush;

    return 0;
}
