"""
【パターン #1】
合計が 9 以下となる連続する 2 つの桁を選ぶと、
次のラウンドの参加者の人数の桁数は 1 減り、各桁の数字の和は変わりません。
【パターン #2】
合計が 10 以上となる連続する 2 つの桁を選ぶと、
次のラウンドの参加者の人数の桁数は変わらず、各桁の数字の和は 9 減ります。

表にまとめてみると、次のようになります。

|パターン|桁数の減少|各桁の数字の和の減少|
|パターン #1|1|0|
|パターン #2|0|9|

つまり、𝑁 の桁数を 𝐷、各桁の数字の和を 𝑆 とすると：

⚫ 桁数は 1 で終わるので、パターン #1 はちょうど 𝐷 − 1 回行われる
⚫ 各桁の数字の和は 1～9 のどれかで終わるので、パターン #2 はちょうど 「𝑆 − 1 を 9 で割った商」 回行われる

よって、予選の回数は (𝐷 − 1) + ⌊(𝑆 − 1) ÷ 9⌋ となります。(⌊𝑥⌋ は 𝑥 を整数で切り捨てた値です)
これを求めるプログラムを書けば、正解となります。
"""
M = int(input())
d = [0] * M
c = [0] * M
for i in range(M):
    d[i], c[i] = map(int, input().split())
D = 0
S = 0
for i in range(M):
    D += c[i]
    S += d[i] * c[i]
print((D - 1) + (S - 1) // 9)   # (S - 1)なのは、S=9のとき0にするため
