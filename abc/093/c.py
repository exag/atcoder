u"""
3つの数値の和は必ず2ずつ増える
操作後の数をXとすると、操作した回数は
{3X-(A+B+C)}/2 回となる
以下を満たす最小の X を求める
条件1: X >= max(A,B,C) ※ 以下 M とする
条件2: 3X ≡ A+B+C (mod2)

X は M または M+1 である（条件2より）
なので、M と A+B+C の偶奇が同じなら X = M
そうでなければ X = M+1 となる
"""
A, B, C = map(int, input().split())

M = max(A, B, C)

if M % 2 == (A + B + C) % 2:
    X = M
else:
    X = M + 1

ans = (3 * X - (A + B + C)) // 2
print(ans)
