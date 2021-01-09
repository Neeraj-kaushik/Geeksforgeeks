def split(n):
    c0, c1 = 0, 0
    j, x = 0, 0
    for i in range(len(n)):
        if n[i] == "0":
            c0 += 1
        if n[i] == "1":
            c1 += 1
        if c0 == c1:
            x += 1
            j = i+1
            c0 = 0
            c1 = 0
    if x > 1:
        print(x)
    else:
        print("-1")


n = input()
split(n)
