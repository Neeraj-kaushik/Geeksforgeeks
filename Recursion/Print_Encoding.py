def pe(n, ans):
    if len(n) == 0:
        print(ans, end=" ")
        return
    elif len(n) == 1:
        ch = int(n[0])
        if ch == 0:
            return
        else:
            val = str(chr(ord('a')+ch-1))
            print(ans+val, end=" ")
    else:
        ch = int(n[0])
        ros = n[1:]
        if ch == 0:
            return
        else:
            val = str(chr(ord('a')+ch-1))
            pe(ros, ans+val)
        ch1 = int(n[0:2])
        ros1 = n[2:]
        if ch1 <= 26:
            val2 = str(chr(ord('a')+ch1-1))
            pe(ros1, ans+val2)


n = input()
pe(n, "")
