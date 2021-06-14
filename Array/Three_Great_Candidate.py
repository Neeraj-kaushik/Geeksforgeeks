def three_great_candidate(li):
    li = sorted(li)
    print(li[-1]*li[-2]*li[-3])


n = int(input())
li = [int(x) for x in input().split()]
three_great_candidate(li)
