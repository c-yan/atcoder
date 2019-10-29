N, H = map(int, input().split())
a, b = zip(*(map(int, input().split()) for _ in range(N)))

a_max = max(a)                   # 振るの最大ダメージ
b = [x for x in b if x > a_max]  # 振るの最大ダメージより、投げつけるダメージが低い刀は投げつける意味がないので除去
b.sort(reverse=True)

result = 0

# 投げつけるダメージが高い順に刀を投げていき、刀が尽きる前に倒せればそれで終了
for x in b:
    result += 1
    H -= x
    if H <= 0:
        break

# もし投げつけるだけで倒せなかった場合は、振るの最大ダメージの刀を振る
# 振るの最大ダメージの刀が投げつける刀に入っていた場合は、必要なだけ振った後に投げつけたことになる
if H > 0:
    result += (H + (a_max - 1)) // a_max

print(result)
