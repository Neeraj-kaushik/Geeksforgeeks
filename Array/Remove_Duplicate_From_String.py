def remove_duplicate(str):
    li = []
    for i in str:
        if i not in li:
            li.append(i)
    for i in range(len(li)):
        print(li[i], end="")


str = input()
remove_duplicate(str)
