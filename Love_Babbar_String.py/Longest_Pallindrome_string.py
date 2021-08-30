def longestPalin(s):
    max = -1
    if len(s) % 2 == 0:
        i = 1
        j = i+1
        while j <= len(s)-1:
            if s[i] != s[j]:
                i += 1
                j += 1
            else:
                a = i
                b = j
                while a >= 0 and b <= len(s)-1:
                    if s[a] == s[b]:
                        if b-a > max:
                            max = b-a
                            res = s[a:b+1]
                        a -= 1
                        b += 1
                    else:
                        i += 1
                        j += 1
                i += 1
                j += 1
    print(res)


s = input()
longestPalin(s)
