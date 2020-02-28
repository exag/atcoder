"""
素数5個の和が
素数であることを保証することは難しいが、
合成数であることを保証することはかんたん

5で割って1余る数を5個足すと、和は必ず5の倍数となる

なのでそのような個数をN個出力すればいい
数えてみると14001個くらいあったので、成約はクリアできる
"""
def is_5mod1_prime(n):
    if n == 1:
        return False
    if n % 5 != 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


N = int(input())
primes = []
for i in range(55555):
    i += 1
    if is_5mod1_prime(i):
        primes.append(i)

ans = primes[:N]
print(' '.join([str(a) for a in ans]))
