def psp(n, ans):
    if n < 0:
        return
    if n == 0:
        print(ans, end=" ")
        return
    psp(n-1, ans+'1')
    psp(n-2, ans+'2')
    psp(n-3, ans+'3')


n = int(input())
psp(n, "")
