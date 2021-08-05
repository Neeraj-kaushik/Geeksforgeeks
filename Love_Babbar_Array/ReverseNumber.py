def Reverse(s):
    s = s[::-1]
    return s


t = int(input())
while t != 0:
    s = input()
    print(Reverse(s))
    t = t-1
