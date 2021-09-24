def tower(n, A, B, C):
    if n == 0:
        return
    tower(n-1, A, C, B)
    print(n, "disk are shifted from", A, "to", B)
    tower(n-1, C, B, A)


n = int(input())
tower(n, "A", "B", "C")
