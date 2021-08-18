def array_subset(li, li1):
    for i in range(len(li1)):
        if li1[i] not in li:
            return "No"
    return "Yes"


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
print(array_subset(li, li1))
