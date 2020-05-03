"""bit全探索
H=10 なので横の割り方は全通りを試せる(2^10=1024)
縦の割り方は、どれだけ割らないで行けるかを左から貪欲に試していく

考察はそれほどでもないけど、実装はかなり重め
"""
from collections import defaultdict


INF = float("inf")

H, W, K = map(int, input().split())
S = []
for i in range(H):
    S.append(input().strip())

ans = INF
for div in range(1 << (H - 1)):
    id = defaultdict(int)
    # 横に割った回数(=グループID)
    g = 0
    for i in range(H):
        id[i] = g
        if div >> i & 1:
            g += 1

    # 元の[H行W列]の板チョコを、[g+1行W列]の板チョコとして考え直す
    c = [[0] * W for _ in range(g + 1)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "1":
                c[id[i]][j] += 1

    # ここに1列分づつ追加していく
    now = defaultdict(int)

    def add(j):
        # 1列分追加してみる
        for i in range(g + 1):
            now[i] += c[i][j]

    def is_over():
        # Kを超えるグループがあったらTrue、なかったらFalse
        for i in range(g + 1):
            if now[i] > K:
                return True
        return False

    num = g
    for j in range(W):
        add(j)
        if is_over():
            # 1列分追加してみて超える場合は、縦に割る
            num += 1
            # 割った最初の列のみ格納して再スタート
            now = defaultdict(int)
            add(j)
            # 1列だけで超える（割る前から超えている）場合があるので、ここでもう一度確認する
            # 超える場合は絶対に無理なので、INFを入れて終了する
            if is_over():
                num = INF
                break

    ans = min(ans, num)

print(ans)
