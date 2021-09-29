def stairs(n):
    if n == 0:
        li1 = []
        li1.append("")
        return li1
    elif n < 0:
        li1 = []
        return li1
    path1 = stairs(n-1)
    path2 = stairs(n-2)
    path3 = stairs(n-3)
    paths = []
    for ele in path1:
        paths.append('1'+ele)
    for ele in path2:
        paths.append('2'+ele)
    for ele in path3:
        paths.append('3'+ele)
    return paths


n = int(input())
li = stairs(n)
print(li)
