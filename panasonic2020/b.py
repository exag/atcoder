H, W = map(int, input().split())
if min(H, W) == 1:
    print(1)
    exit()
print((H * W + 1) // 2)
