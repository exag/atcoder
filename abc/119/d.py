"""
神社、寺それぞれについて、左右に一番近いものだけを考えればいい
神社L→寺L
神社L→寺R
神社R→寺L
神社R→寺R
寺L→神社L
寺L→神社R
寺R→神社L
寺R→神社R
の8通りのうち、最小のものを出力すればいい

神社R、寺Rは2分探索で求めて、
神社L、寺Lはその1つ手前
"""

import bisect


A, B, Q = map(int, input().split())
INF = float("inf")
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]
for q in range(Q):
    x = int(input())
    # xの右隣の神社
    b = bisect.bisect_right(s, x)
    # xの右隣の寺
    d = bisect.bisect_right(t, x)
    ans = INF
    for S in (s[b - 1], s[b]):
        for T in (t[d - 1], t[d]):
            # 神社→寺
            d1 = abs(S - x) + abs(T - S)
            # 寺→神社
            d2 = abs(T - x) + abs(S - T)
            ans = min(ans, d1, d2)
    print(ans)
