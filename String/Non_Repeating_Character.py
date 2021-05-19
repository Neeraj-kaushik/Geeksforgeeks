def character(s):
    for i in range(len(s)-1):
        li=[]
        for j in range(i+1,len(s)):
            li.append(s[j])
        if s[i] in li:
            continue
        else:
            print(s[i])
            break

            

                


s=input()
character(s)