#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int H, W;
    cin >> H >> W;

    map<int, int> candidates;
    map<int, int> moves;

    rep(i, W) {
        candidates[i] = i;
    }
    moves[0] = W;

    rep(i, H) {
        int A, B;
        cin >> A >> B;
        A--;

        int r = -1;
        while (true) {
            auto it = candidates.lower_bound(A);
            if (it == candidates.end() || it->first > B) break;

            r = max(r, it->second);
            int t = it->first - it->second;
            moves[t]--;
            if (moves[t] == 0) {
                moves.erase(t);
            }
            candidates.erase(it);
        }
        if (r != -1 && B != W) {
            moves[B - r]++;
            candidates[B] = r;
        }

        if (moves.size() == 0) {
            cout << -1 << "\n";
        } else {
            cout << moves.begin()->first + (i + 1) << "\n";
        }
    }
    cout << flush;

    return 0;
}
