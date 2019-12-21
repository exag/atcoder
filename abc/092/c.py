"""方針
全体の移動距離をDとすると、
D = |0-A1| + |A1-A2| + |A2-A3| + |A3-0|
A2を省いたときの移動距離は、
D -  |A1-A2| - |A2-A3| + |A1-A3|
これを各Aについて計算すれば良い
"""

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)

D = 0
for i in range(N+1):
    D += abs(A[i+1] - A[i])

for i in range(1, N+1):
    dist = D - (abs(A[i-1] - A[i]) + abs(A[i] - A[i+1])) + abs(A[i-1] - A[i+1])
    print(dist)

