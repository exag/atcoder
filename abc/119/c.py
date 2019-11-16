N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
INF = 10 ** 9


# 先に全ての合成を終えてから延長/縮小をすると考える
# それぞれの竹は、[Aに使う, Bに使う, Cに使う, どれにも使わない]の4通り
# 4 ** 8 = 65536 なので全通り試しても間に合う
def dfs(cur, len_a, len_b, len_c):
    if cur == N:
        if min(len_a, len_b, len_c) > 0:
            # 1本目は合成していないので、10ずつ引いて調整する
            return abs(len_a - A) + abs(len_b - B) + abs(len_c - C) - 30
        else:
            # 竹を1本も使わなかったケースを除外する
            return INF
    # どれにも使わない
    not_use = dfs(cur + 1, len_a, len_b, len_c)
    # Aに使う（Aを使うために合成する）
    use_for_a = dfs(cur + 1, len_a + L[cur], len_b, len_c) + 10
    # Bに使う（Bを使うために合成する）
    use_for_b = dfs(cur + 1, len_a, len_b + L[cur], len_c) + 10
    # Cに使う（Cを使うために合成する）
    use_for_c = dfs(cur + 1, len_a, len_b, len_c + L[cur]) + 10

    return min(not_use, use_for_a, use_for_b, use_for_c)


print(dfs(0, 0, 0, 0))
