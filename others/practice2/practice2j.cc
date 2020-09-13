#include <atcoder/all>
#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using ll = long long;
using namespace std;
using namespace atcoder;

int op(int a, int b) { return max(a, b); }

int e() { return -1; }

int target;

bool f(int v) { return v < target; }

int main()
{
    int N, Q;
    cin >> N >> Q;

    vector<int> A(N);
    rep(i, N) {
        cin >> A[i];
    }

    segtree<int, op, e> st(A);
    rep(_, Q) {
        int T;
        cin >> T;
        if ((T == 1) || (T == 3)) {
            int X, V;
            cin >> X >> V;
            if (T == 1) {
                st.set(X - 1, V);
            } else if (T == 3) {
                target = V;
                cout << st.max_right<f>(X - 1) + 1 << '\n';
            }
        } else if (T == 2) {
            int L, R;
            cin >> L >> R;
            cout << st.prod(L - 1, R) << '\n';
        }
    }
    cout << endl;

    return 0;
}
