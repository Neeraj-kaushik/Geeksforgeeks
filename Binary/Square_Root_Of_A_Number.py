def floorsqrt(x):
    a=x//2
    for i in range(2,a+2):
        if i*i==x:
            print(i)
            break
        elif i*i>x:
            print(i-1)
            break

        

x=int(input())
floorsqrt(x)