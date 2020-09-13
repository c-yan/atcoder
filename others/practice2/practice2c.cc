#include <atcoder/all>
#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using ll = long long;
using namespace std;
using namespace atcoder;

int main()
{
    int T;
    cin >> T;

    rep(_, T) {
		int N, M, A, B;
        cin >> N >> M >> A >> B;
        cout << floor_sum(N, M, A, B) << '\n';
    }
    cout << endl;

    return 0;
}
