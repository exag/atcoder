"""DFS
営業する/しないを全列挙する
"""


def calc(days):
    # 必ず1回は営業する
    if sum(days) == 0:
        return
    profit = 0
    for i in range(N):
        both = 0
        for f, d in zip(F[i], days):
            if f == d == 1:
                both += 1
        profit += P[i][both]
    global ans
    ans = max(ans, profit)


def dfs(days):
    if len(days) == 10:
        calc(days)
        return
    dfs(days + [0])
    dfs(days + [1])


ans = 10 ** 9 * (-1)
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

dfs([])
print(ans)
