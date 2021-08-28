def reverse_str(a):
    s = 0
    e = len(a)-1
    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1
    print(a)


a = ['a', 'b', 'c', 'd']
reverse_str(a)
