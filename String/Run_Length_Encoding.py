def encoding(st):
    for i in range(len(st)-1):
        a=0
        for j in range(i+1,len(st)):
            while st[i]!=st[j]:
                a=j-i
                print(st[i]+str(a),end='')
                i=j
            
                            


st=input()
encoding(st)