def factorial(n):
    fact = 1
    while n > 0:
        fact = fact*n
        n -= 1
    li = []
    while fact != 0:
        ren = fact % 10
        li.append(ren)
        fact = fact//10
    li.reverse()
    print(li)


n = int(input())
factorial(n)
