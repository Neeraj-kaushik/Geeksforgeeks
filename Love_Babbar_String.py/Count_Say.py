def count_say(n):
    if n == 1:
        return "1"
    s = count_say(n-1)
    res = ""
    counter = 0
    for i in range(0, len(s)):
        counter += 1
        if i == len(s)-1 or s[i] != s[i+1]:
            counter = str(counter)
            res = res+counter+s[i]
            counter = 0
    return res


n = int(input())
print(count_say(n))
