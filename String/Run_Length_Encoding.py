def encoding(st):
    for i in range(len(st)-1):
        j=i
        while st[i]!=st[j] and j<len(st):
            if st[i]!=st[j]:
                a=j-i
            else:
                j=j+1
        print(st[i]+str(a),end='')
        i=j            
        
                            


st=input()
encoding(st)