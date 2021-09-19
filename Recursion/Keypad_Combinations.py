def kc(val, li1):
    if len(val) == 0:
        li3 = []
        li3.append("")
        return li3
    ch = int(val[0])
    ros = val[1:]
    li4 = kc(ros, li1)
    val2 = str(li1[ch])
    li5 = []
    for i in range(len(val2)):
        val3 = val2[i]
        for ele in li4:
            li5.append(val3+ele)
    return li5


val = input()
li1 = ['.:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tu', 'vwz', 'yz']
li2 = kc(val, li1)
print(li2)
