# 方針
# |(A1-1)-x| + |(A2-2)-x| + ... を最小とするxを求める
# 数直線で考えた時、(A1-1)、(A2-2)、...への距離の合計が最小となるx
# →xは中央値

from statistics import median_low


N = int(input())
A = list(map(int, input().split()))
# 中央値
B = []
for i in range(N):
    B.append(A[i] - (i+1))
b = median_low(B)

ans = 0
for i in range(N):
    ans += abs(A[i] - (i + 1) - b)

print(ans)

