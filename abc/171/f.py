"""
N = len(S) とする
操作手順を考えるのではなく、最終的に出来上がる
N + K 桁の文字列に、S という部分文字列が含まれると考える
S が 3 桁 (abc) だとすると、K 回の操作で入れれる文字は _ の部分

_a_b_c_

最後の _ は 26 通り、他の _ は 25 通り
なぜなら S という部分文字列の数え方を貪欲的に考えると、
a は 1 番最初に出現した a を選ぶのが最適 -> 最初の _ は a 以外ということになる。
b の前の _ と c の前の _ についても同様
c よりあとの _ については、abc が出現し終わってるので、何でもいい -> 26通り

最後の _ とそれ以外の _ は分けて考える。

_a_b_ と c_

K のうちi個を前半で使うとして、i を 0 から K まで試していく

前半は以下の組み合わせの和になる
_ の個数 * 25 -> 25 ** i
abの並べ方 -> i 個の _ と N-1 (Sの最終文字以外) から N-1 個を選ぶ -> i+N-1 Choose N-1

後半は
_ の個数 * 26 -> 26 ** (K-i)
"""

from collections import defaultdict

MOD = 10 ** 9 + 7

def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    return fact[a] * ifact[b] * ifact[a-b]


K = int(input())
S = input().strip()
N = len(S)

# 階乗を前処理
fact = defaultdict(int)
fact[0] = 1
for i in range(1, N+K+1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD
# 階乗の逆元を前処理
ifact = defaultdict(int)
ifact[N+K] = pow(fact[N+K], MOD-2, MOD)
for i in reversed(range(1, N+K+1)):
    ifact[i-1] = ifact[i] * i
    ifact[i-1] %= MOD

ans = 0
for i in range(K+1):
    now = pow(26, K-i, MOD)
    now *= pow(25, i, MOD)
    now %= MOD
    now *= combination(i+N-1, N-1)
    now %= MOD
    ans += now
    ans %= MOD

print(ans)
