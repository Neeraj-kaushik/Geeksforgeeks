def print_subset(li, ind, sub, sum1, tgt):
    if ind == len(li):
        if sum1 == tgt:
            print(sub)
        return
    print_subset(li, ind+1, sub+str(li[ind])+",", sum1+li[ind], tgt)
    print_subset(li, ind+1, sub, sum1, tgt)


n = int(input())
li = [int(x) for x in input().split()]
tgt = int(input())
print_subset(li, 0, "", 0, tgt)
