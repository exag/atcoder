"""DFS
"""
from string import ascii_lowercase as alphabets


N = int(input())


def dfs(s, used):
    if len(s) == N:
        print(s)
        return
    # 今まで使った文字種＋次の文字まで
    for i in range(used+2):
        t = s
        t += alphabets[i]
        dfs(t, max(used, i))


dfs("a", 0)
