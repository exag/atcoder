"""
各桁の取りうる値は、

左端の桁: 0〜その数字まで
それ以外: 0〜9

なのでN以下という条件を一旦無視すると、

先頭の桁＋残りの桁が全部9
ex. 399999

が最大値の候補 (m とする)

もしこれが無理（Nを超える）とすると、
先頭の桁を1小さくすると可能になる

ex. 31415 の場合 39999 は無理だけど 29999 は可能

よって m-1 が答え
もし最初から x9999 の形になっていれば、 m が答え

"""
si = lambda: input().strip()

S = si()

digit = len(S)

head, remaining = S[0], S[1:]

ans = int(head) + 9 * (digit-1)
if remaining != '9' * (digit-1):
    ans -= 1

print(ans)

