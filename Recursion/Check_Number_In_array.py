def cnum(li, x):
    if len(li) == 0:
        return False
    if li[0] == x:
        return True
    smalla = cnum(li[1:], x)
    return smalla


li = [int(x) for x in input().split()]
x = int(input())
if cnum(li, x):
    print("true")
else:
    print("false")
