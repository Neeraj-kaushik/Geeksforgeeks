def valid_shuffle(s1, s2, s3):
    if len(s1)+len(s2) != len(s3):
        print("No")
    else:
        i, j, k, f = 0, 0, 0, 0
        while k < len(s3):
            if i < len(s1) and s1[i] == s3[k]:
                i += 1
            elif j < len(s2) and s2[j] == s3[k]:
                j += 1
            else:
                f = 1
                break
            k += 1
        if i < len(s1) or j < len(s2):
            print("No")
        else:
            print("Yes")


s1 = str(input())
s2 = str(input())
s3 = str(input())
valid_shuffle(s1, s2, s3)
