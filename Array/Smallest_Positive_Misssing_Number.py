def missing_number(li):
    positive_int = []
    max_element = 0
    for i in li:
        if i > 0:
            positive_int.append(i)
            
        if i > max_element:
            max_element = i
           
    elements = [0] * (max_element + 1)

    for i in positive_int:
        elements[i-1] = 1
    
            
    for i in range(len(elements)):
        if elements[i] == 0:
            print(i + 1)
            break
            
    
        

        

n=int(input())
li=[int(x) for x in input().split()]
missing_number(li)