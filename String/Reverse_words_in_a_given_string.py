def reverse_string(str):
    li=str.split('.')
    l=li[::-1]
    for i in li:
        print(i,'.',end='')

str=input()
reverse_string(str)