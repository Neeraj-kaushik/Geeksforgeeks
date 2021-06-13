def smallest_window(str):
    li = []
    for i in range(len(str)):
        if str[i] not in li:
            li.append(str[i])
    print(len(li))


str = input()
smallest_window(str)
