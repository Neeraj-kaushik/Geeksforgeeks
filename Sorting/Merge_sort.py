def merge_sort(li):
    if len(li)>1:
        mid=len(li)//2
        l=li[:mid]
        r=li[mid:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i<len(l) and j <len(r):
            if l[i]<r[j]:
                li[k]=l[i]
                i=i+1
            else:
                li[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            li[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            li[k]=r[j]
            j=j+1
            k=k+1
    return(li)



a=int(input())
li=[int(x) for x in input().split()]
merge_sort(li)
print(li)