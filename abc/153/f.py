"""キューを使って左端から貪欲法
"""
from math import ceil
from collections import deque


N, D, A = map(int, input().split())
monsters = []
for i in range(N):
    x, h = map(int, input().split())
    monsters.append((x, h))
monsters.sort()


damage_sum = 0
ans = 0
q = deque([])
for i in range(N):
    x, h = monsters[i]
    while q and q[0][0] < x:
        # 有効期限が切れたら、キューから取り出し、累積ダメージから減算する
        damage_sum -= q[0][1]
        q.popleft()
    # 累積ダメージをモンスターのHPから減算する
    h -= damage_sum
    if h > 0:
        # HPが残っていたら追加攻撃する
        hit = ceil(h / A)
        ans += hit
        damage = hit * A
        damage_sum += damage
        # (有効期限、そのモンスターに与えたダメージ)
        q.append((x + 2 * D, damage))

print(ans)
