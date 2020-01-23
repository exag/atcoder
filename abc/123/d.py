"""
A*B*C(1000^3) は間に合わないけど、
A*B(1000^2) を先にに計算して、その上位3000位*1000 なら間に合う
※ pypy3 じゃないと間に合わない
"""
X, Y, Z, K = map(int, input().split())

A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)

AB = []
for i in range(X):
    for j in range(Y):
        AB.append(A[i] + B[j])

AB.sort(reverse=True)

ABC = []
for i in range(min(K, len(AB))):
    for j in range(Z):
        ABC.append(AB[i] + C[j])

ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])
