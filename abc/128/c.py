# bit演算
N, M = map(int, input().split())
# 各スイッチがどの電球に繋がっているかをbitで持つ
# スイッチ1が電球1、電球2に繋がっている場合は
# 101 -> 5 という持ち方
a = [0] * N
for i in range(M):
    K, *S = list(map(int, input().split()))
    for j in range(K):
        s = S[j]
        s -= 1
        # s番目のスイッチにi番目の電球が繋がっている
        a[s] |= 1 << i

expected = 0
l = list(map(int, input().split()))
for i in range(M):
    expected |= l[i] << i

# on/offの2通り、スイッチは最大10個なので、# 2^10=1024で全通り試してもOK
# on/offの全ての組み合わせをbitでループする
ans = 0
for s in range(1 << N):
    # 各電球の状態(bit)
    lighting = 0
    for i in range(N):
        # iビット目が立っているか
        if s >> i & 1:
            # i番目のスイッチが付いていれば、つながった電球の状態を反転させる
            lighting ^= a[i]
    # 各スイッチを押した後の電球の状態が理想と一致するか
    if lighting == expected:
        ans += 1

print(ans)
