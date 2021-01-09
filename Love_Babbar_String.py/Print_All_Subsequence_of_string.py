def subsequence(n, x):
    if len(n) == 0:
        print(x, end=' ')
        return
    subsequence(n[1:], x+n[0])
    subsequence(n[1:], x)


n = input()
x = ""
subsequence(n, x)
