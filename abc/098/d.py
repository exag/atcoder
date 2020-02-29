"""しゃくとり法
"""
N = int(input())
A = list(map(int, input().split()))

ans = 0
left, right = 0, 0
total = 0
while left < N:
    if right < N and total + A[right] == total ^ A[right]:
        total += A[right]
        right += 1
    else:
        ans += right - left
        total -= A[left]
        left += 1
print(ans)
