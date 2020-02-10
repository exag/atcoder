"""
dp[i][j][k]
i: 0～桁数
j: 0～K
k: 0, 1

i桁目までを決めて
j個の非0を使って
k=0 -> そこまでの桁はNと一致
k=1 -> そこまでの桁ですでにN以下であることが確定
"""
from copy import deepcopy


# 多次元配列を作成する
def make_multi_list(initial, degree):
    ans = [initial for _ in range(degree[-1])]
    for d in reversed(degree[:-1]):
        ans = [deepcopy(ans) for _ in range(d)]
    return ans


EQUAL = 0
SMALLER = 1

S = input().strip()
K = int(input())
MAX_DIGIT = len(S)

dp = make_multi_list(initial=0, degree=[105, 4, 2])
# 初期状態
dp[0][0][0] = 1


# 配るDP
for i in range(MAX_DIGIT):
    for j in range(4):
        for k in [EQUAL, SMALLER]:
            # 今の桁
            now_digit = int(S[i])
            # 次の桁を0～9のどれにするかが遷移の全て
            for next_digit in range(10):
                # 遷移先を決める
                # 桁は普通に1つ増やす
                ni = i + 1
                # 非ゼロを使った個数は選ぶ数字によって変わる
                nj = j
                if next_digit != 0:
                    # 非ゼロを1つ使ったのでjを加算する
                    nj += 1
                if nj > K:
                    # 非ゼロがK個を超えるような先には遷移しない
                    continue
                # 現時点（i桁まで）でNと等しいかどうかも選ぶ数字によって変わる
                nk = k
                if k == EQUAL:
                    if next_digit > now_digit:
                        # Nを超えるような先には遷移しない
                        continue
                    if next_digit < now_digit:
                        # N以下であることが確定する
                        nk = SMALLER
                    if next_digit == now_digit:
                        # そのまま(EQUALのまま)
                        pass
                if k == SMALLER:
                    # すでにN未満であることが確定しているのでSMALLERのまま（何を選んでもN未満になる）
                    pass
                # print('dp[{}][{}][{}] ({}) += dp[{}][{}][{}] ({})'.format(
                #     ni, nj, 'SMALL' if nk else 'EQUAL', dp[ni][nj][nk], i, j, 'SMALL' if k else 'EQUAL', dp[i][j][k]))
                dp[ni][nj][nk] += dp[i][j][k]

ans = dp[MAX_DIGIT][K][EQUAL] + dp[MAX_DIGIT][K][SMALLER]
print(ans)

