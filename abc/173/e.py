"""
https://youtu.be/IMwigbYzLbI?t=4136
丁寧に場合分けをする

正の数を S 個
負の数を T 個
とする


積を正にできるか？ 積を正にする = 負を偶数個選ぶということ

* S > 0 の場合
    ** N = K の場合
        選択の余地なし(全部選ぶことになる)
        T が偶数なら OK
    ** N != K の場合
        常に OK
        積が負になる場合は、余った数と入れ替えれることで正にできるから
* S = 0 の場合
    K が偶数なら OK


* 正にできない場合
    どうやっても負なので、絶対値が小さい順に選ぶ
* 正にできる場合
    負の数は 2 個セットで取ると良い
        -> 絶対値が大きい順に取る
    正の数も 2 個セットで取ると良い
        -> K が奇数のときは 先に正の数を 1 つ取って数を合わせる
"""
MOD = 10 ** 9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
T = []

for a in A:
    if a < 0:
        T.append(a)
    else:
        S.append(a)

lenS = len(S)
lenT = len(T)

ok = False
if lenS > 0:
    if N == K:
        ok = lenT % 2 == 0
    else:
        ok = True
else:
    ok = K % 2 == 0

ans = 1
if not ok:
    A.sort(key=lambda x: abs(x))
    for i in range(K):
        ans *= A[i]
        ans %= MOD
else:
    S.sort()
    T.sort(reverse=True)
    if K % 2 == 1:
        ans *= S.pop()
    P = []
    while len(S) >= 2:
        x = S.pop()
        x *= S.pop()
        P.append(x)
    while len(T) >= 2:
        x = T.pop()
        x *= T.pop()
        P.append(x)
    P.sort(reverse=True)
    for i in range(K//2):
        ans *= P[i]
        ans %= MOD

print(ans)



