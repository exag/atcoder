"""枝借り
Aのランク*Bのランク*Cのランク <= K
となるA, B, Cだけ考えればいい

例えばK=8なら、それぞれ1〜2位を選ぶしかない
3位以降を選ぶと絶対に8位以内には入れない

これならpypyじゃなくても間に合う
"""
X, Y, Z, K = map(int, input().split())

A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)

ABC = []
for a in range(X):
    for b in range(Y):
        if (a + 1) * (b + 1) > K:
            break
        for c in range(Z):
            if (a + 1) * (b + 1) * (c + 1) > K:
                break
            ABC.append(A[a] + B[b] + C[c])

ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])
