import math

def function_power(n):
    rev=mod=0
    i=n
    while i!=0:
        mod=i%10
        rev=rev*10+mod
        i=i//10
    c=pow(n,rev)%1000000007
    print(c)

n=int(input())
function_power(n)