def index_of_element(n,li,li1):
    for i in range(len(li)):
        if li[i] not in li1:
            print(i)
    

n=int(input())
li=[int(x) for x in input().split()]
li1=[int(x) for x in input().split()]
index_of_element(n,li,li1)