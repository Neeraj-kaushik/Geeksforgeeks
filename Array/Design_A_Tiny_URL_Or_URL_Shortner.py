import random


def Url_shortner(n):
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    print(''.join(random.choice(a) for i in range(3)))


n = int(input())
Url_shortner(n)
