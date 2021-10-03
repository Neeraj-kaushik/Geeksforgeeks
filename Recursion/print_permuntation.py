def pp(n, ans):
    if len(n) == 0:
        print(ans, end=" ")
        return
    for i in range(len(n)):
        ch = n[i]
        lstr = n[0:i]
        rstr = n[i+1:]
        mstr = lstr+rstr
        pp(mstr, ans+ch)


n = input()
pp(n, "")
