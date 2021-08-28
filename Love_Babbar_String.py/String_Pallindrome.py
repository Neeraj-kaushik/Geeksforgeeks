def palindrome(s):
    a = s[::-1]
    if a == s:
        print('1')
    else:
        print('0')


s = str(input())
palindrome(s)
