N = int(input())
a = list(map(int, input().split()))
mx = 0
ans = 0
for n in a:
    if n > mx:
        ans += 1
        mx = n
print(ans)