def duplicate(str):
    st = ""
    for i in range(len(str)):
        if str[i] not in st:
            st = st+str[i]
    print(st)


str = input()
duplicate(str)
