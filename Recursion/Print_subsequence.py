def pss(n, ans):
    if len(n) == 0:
        print(ans, end=" ")
        return
    ch = n[0]
    ros = n[1:]
    pss(ros, ans+"")
    pss(ros, ans+ch)


n = input()
pss(n, "")
