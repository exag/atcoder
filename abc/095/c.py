u"""
ABピザの枚数を固定する
1枚も使わない場合〜全部ABピザで賄う場合までを全部試す
"""

A, B, C, X, Y = map(int, input().split())

ans = float('inf')
for ab in range(0, max(X, Y)*2+1, 2):
    a = max(0, X - ab//2)
    b = max(0, Y - ab//2)
    ans = min(ans, A * a + B * b + C * ab)

print(ans)
