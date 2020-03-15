"""
pypyじゃないとTLE
"""
N = int(input())
L = list(map(int, list(input().strip())))

cnt = 0
for d1 in range(10):
    for d2 in range(10):
        for d3 in range(10):
            find1 = False
            find2 = False
            for i, n in enumerate(L):
                if not find1 and L[i] == d1:
                    find1 = True
                    continue
                if find1 and not find2 and L[i] == d2:
                    find2 = True
                    continue
                if find1 and find2 and L[i] == d3:
                    cnt += 1
                    break
print(cnt)
