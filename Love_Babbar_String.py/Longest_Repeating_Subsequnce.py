def longest_repeating_subsequnce(n):
    max = -1
    c = 0
    for i in range(len(n)-1):
        for j in range(len(n)):
            if n[i] == n[j]:
                c += 1
            if n[i] != n[j]:
                if c > max:
                    max = c
                c = 0
    print(max-1)


n = input()
longest_repeating_subsequnce(n)
