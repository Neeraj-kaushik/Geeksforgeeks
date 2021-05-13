def encoding(st):
    i=0
    while i<=len(st)-1:
        j=i
        count=1
        while j<len(st)-1:
            if st[i]==st[j+1]:
                count+=1
                j=j+1
            else:
                break
        print(st[i]+str(count),end='')
        i=j+1         
        
                            
st=input()
encoding(st)