"""
大きい数が書かれた箱からボールを入れるかを決めていくことにします。

こうすると、整数 i が書かれた箱にボールを入れるか決めるとき、
i 以外の i の倍数が書かれた箱については、すでにボールを入れるかが決まっています。

それらの箱に入ったボールの総和の偶奇が ai と異なる場合は箱にボールを入れて、
そうでないときはボールを入れないことにします。

このようにしてボールを入れるかを決めていくと、
与えられた条件をすべて満たすようにボールを入れることができます。
"""
N = int(input())
# 1-indexで進める
a = [0]
a.extend(list(map(int, input().split())))
b = [0 for _ in range(N+1)]

for i in reversed(range(1, N+1)):
    total = 0
    # i自身を除いたiの倍数の箱に入ってるボールの数を数える
    for j in range(i+i, N+1, i):
        # 何個かは重要ではなく、偶奇だけを考えれば良いので、XORを取る
        total ^= b[j]
    # 偶奇が異なる場合は箱にボールを入れて、同じ場合は入れないので、ここもXORを取る
    b[i] = total ^ a[i]

ans_n = 0
ans_l = []
for i in range(N+1):
    if b[i]:
        ans_n += 1
        ans_l.append(str(i))

print(ans_n)
print(' '.join(ans_l))
