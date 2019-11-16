# 完成後の状態から更地に戻す方向で考える
# 高さ0で区切ってグループ化したときのグループ数が、その周で必要な手数
# 全ての花が高さ0になったら終わり
N = int(input())
H = list(map(int, input().split()))
# 一番左のグループをカウントするときに都合がいいように先頭に0を追加
H.insert(0, 0)

ans = 0
while max(H) > 0:
    group = 0
    for i in range(1, N+1):
        if H[i-1] == 0 and H[i] > 0:
            group += 1
    ans += group
    for i in range(1, N+1):
        if H[i] > 0:
            H[i] -= 1

print(ans)

