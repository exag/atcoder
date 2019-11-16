# あらかじめ753数をDFSで列挙する
def make_753number(n):
    s = str(n)
    if '7' in s and '5' in s and '3' in s:
        n753.add(n)
    if n <= 10**9:
        make_753number(10 * n + 7)
        make_753number(10 * n + 5)
        make_753number(10 * n + 3)


n753 = set()
make_753number(0)
N = int(input())
print(len([1 for n in n753 if n <= N]))
