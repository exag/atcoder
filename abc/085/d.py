"""
* 通常攻撃はaが最大の剣だけを使う(max_a)
* 投げつけはbがmax_aより大きいものだけ使う
* 投げつけた終わった残りのHPをmax_aで攻撃するのが最適
"""
N, H = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort(reverse=True)
B.sort(reverse=True)

max_a = A[0]

ans = 0
i = 0
# Throw
T = [b for b in B if b > max_a]
for t in T:
    H -= t
    ans += 1
    if H <= 0:
        print(ans)
        exit()
# 切り上げ
ans += -(-H//max_a)
print(ans)
