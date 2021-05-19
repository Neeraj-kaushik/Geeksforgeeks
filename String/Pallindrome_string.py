def ispallindrome(s):
    a=s[::-1]
    if a==s:
        return True
    else: 
        return False


s=input()
if ispallindrome(s) is True:
    print('1')
else:
    print('0')