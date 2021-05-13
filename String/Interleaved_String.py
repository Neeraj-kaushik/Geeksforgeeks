def interleaved_strings(a,b,c):
    d=a+b
    e=b+a
    if d==c or e==c:
        print('1')
    else:
        print('0')

a=input()
b=input()
c=input()
interleaved_strings(a,b,c)