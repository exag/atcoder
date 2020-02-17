S = input().strip()

num = list(map(int, list(S)))
num.reverse()
num.append(0)

ans = 0
for i in range(len(S)):
    n = num[i]
    if n < 5:
        ans += n
    if n > 5:
        ans += 10-n
        num[i+1] += 1
    if n == 5:
        ans += 5
        if num[i+1] >= 5:
            num[i+1] += 1


print(ans+num[-1])
