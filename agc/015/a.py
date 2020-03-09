N, A, B = map(int, input().split())

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    exit()

if A > B:
    print(0)
    exit()

# 全部A〜全部Bまでの範囲
ans = B * (N - 2) - A * (N - 2) + 1
print(ans)
