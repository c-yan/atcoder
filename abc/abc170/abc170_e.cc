#include <bits/stdc++.h>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, Q;
    cin >> N >> Q;

    multiset<int> max_ratings;
    vector<multiset<int>> kindergartens(2 * pow(10, 5) + 1);
    vector<int> ratings(N + 1), belongs(N + 1);

    rep(i, N) {
        int A, B;
        cin >> A >> B;
        ratings[i + 1] = A;
        belongs[i + 1] = B;
        kindergartens[B].insert(A);
    }

    rep(i, 2 * pow(10, 5) + 1) {
        if (kindergartens[i].size() != 0) {
            max_ratings.insert(*kindergartens[i].rbegin());
        }
    }

    rep(_, Q) {
        int C, D;
        cin >> C >> D;
        int b = belongs[C];
        belongs[C] = D;
        max_ratings.erase(max_ratings.find(*kindergartens[b].rbegin()));
        kindergartens[b].erase(ratings[C]);
        if (kindergartens[b].size() != 0) {
            max_ratings.insert(*kindergartens[b].rbegin());
        }
        if (kindergartens[D].size() != 0) {
            max_ratings.erase(max_ratings.find(*kindergartens[D].rbegin()));
        }
        kindergartens[D].insert(ratings[C]);
        max_ratings.insert(*kindergartens[D].rbegin());
        cout << *max_ratings.begin() << '\n';
    }

    return 0;
}
