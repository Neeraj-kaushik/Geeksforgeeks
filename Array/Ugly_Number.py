def ugly_number(n):
    li = [1]
    value = 1
    while len(li) != n:
        if value % 2 == 0 or value % 3 == 0 or value % 5 == 0:
            li.append(value)
        value += 1
    print(li[-1])


n = int(input())
ugly_number(n)
