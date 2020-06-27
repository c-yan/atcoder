// 平衡二分探索木
#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
	ll N;
	cin >> N;
	vector<ll> A(N);
	rep(i, N) cin >> A[i];

	multiset<ll> t;
	for (auto a : A) {
		auto it = t.lower_bound(a);
		if (it != t.begin()) {
			t.erase(--it);
		}
		t.insert(a);
	}
	cout << t.size() << endl;

	return 0;
}
