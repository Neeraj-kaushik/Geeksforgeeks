def kpc(n, li1, ans):
    if len(n) == 0:
        print(ans, end=" ")
        return
    ch = int(n[0])
    ros = n[1:]
    val = li1[ch]
    for i in range(len(val)):
        val2 = val[i]
        kpc(ros, li1, ans+val2)


n = input()
li1 = ['.:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tu', 'vwz', 'yz']
kpc(n, li1, "")
