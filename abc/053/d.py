from collections import defaultdict

N = int(input())
A = sorted(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

ans = 0
duplicate = 0
q = list()
for k, v in d.items():
    if v % 2 == 1:
        # 奇数枚なら最終的に1枚になるので、そのまま答えに加算する
        ans += 1
    else:
        # 偶数枚なら最終的に2枚になるので、あとで計算する
        duplicate += 1

# 2枚残っているカード通しを消せばそれぞれが答えになる
ans += duplicate
# 最後に2枚余っているカードがあれば、1枚のカードも消さないといけないので1引く
if duplicate % 2 == 1:
    ans -= 1

print(ans)
