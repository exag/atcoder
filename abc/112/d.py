"""
"""
N, M = map(int, input().split())

# Mの約数列挙
divs = set()
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        divs.add(i)
        divs.add(M // i)

ans = 0
for d in divs:
    if N * d <= M:
        ans = max(ans, d)

print(ans)
