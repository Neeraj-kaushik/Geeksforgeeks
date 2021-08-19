def pallindrome_array(li):
    for i in range(len(li)):
        k = li[i]
        rev = 0
        while k != 0:
            res = k % 10
            rev = rev*10+res
            k = k//10
        if rev != li[i]:
            flag = False
        else:
            flag = True
    return flag


li = [int(x) for x in input().split()]
if pallindrome_array(li):
    print(1)
else:
    print(0)
