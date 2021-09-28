def gss(val):
    if len(val) == 0:
        li3 = []
        li3.append("")
        return li3

    ch = val[0]
    ros = val[1:]
    li1 = gss(ros)
    li2 = []
    for ele in li1:
        li2.append(""+ele)
    for el in li1:
        li2.append(ch+el)
    return li2


val = input()
li = gss(val)
print(li)
