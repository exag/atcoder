"""
区間スケジューリング問題みたいなもの
終端でソートする
"""
N, M = map(int, input().split())

bridges = []
for i in range(M):
    a, b = map(int, input().split())
    bridges.append((a, b))

bridges.sort(key=lambda x: x[1])

ans = 0
x = 0
for i in range(M):
    a, b = bridges[i]
    if a >= x:
        x = b
        ans += 1

print(ans)

