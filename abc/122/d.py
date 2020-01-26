"""DFS(メモ化再帰)
解説放送はDPで解いている
https://www.youtube.com/watch?v=w2AEXSloYk8
"""
from functools import lru_cache


N = int(input())
MOD = 10**9+7


def ok(last4):
    for i in range(4):
        t = list(last4)
        if i > 0:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') > 0:
            return False
    return True


@lru_cache(maxsize=1000)
def dfs(cur, last3):
    if cur == N:
        return 1
    ret = 0
    for c in 'AGCT':
        if ok(last3 + c):
            ret += dfs(cur+1, last3[1:] + c)
            ret %= MOD
    return ret


print(dfs(0, 'TTT'))
