def rotation(s1, s2):
    temp = s1+s1
    if s2 in temp:
        print('1')
    else:
        print('0')


s1 = str(input())
s2 = str(input())
rotation(s1, s2)
